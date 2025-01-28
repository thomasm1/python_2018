# dataset.py
import pandas as pd
from torch.utils.data import Dataset

class BlockchainDataset(Dataset):
    def __init__(self, csv_file):
        # Load dataset
        self.data = pd.read_csv(csv_file)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        row = self.data.iloc[idx]
        # Extract input features and labels (e.g., predict "value")
        features = {
            'from_address': row['from_address'],
            'to_address': row['to_address'],
            'gas': row['gas'],
            'gas_price': row['gas_price']
        }
        label = row['value']
        return features, label

# pipeline.py
import torch
from torch.utils.data import DataLoader
from sklearn.preprocessing import LabelEncoder

def preprocess_data(dataset):
    # Encode addresses as integers
    from_encoder = LabelEncoder()
    to_encoder = LabelEncoder()

    dataset.data['from_address'] = from_encoder.fit_transform(dataset.data['from_address'])
    dataset.data['to_address'] = to_encoder.fit_transform(dataset.data['to_address'])

    return dataset

def create_dataloader(dataset, batch_size=32):
    return DataLoader(dataset, batch_size=batch_size, shuffle=True)

# model.py
import torch.nn as nn

class TransactionPredictor(nn.Module):
    def __init__(self, input_dim):
        super(TransactionPredictor, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 1)  # Output a single value (transaction value)
        )

    def forward(self, x):
        return self.fc(x)

# training.py
import torch
import torch.optim as optim
from torch.nn import MSELoss
from dataset import BlockchainDataset
from pipeline import preprocess_data, create_dataloader
from model import TransactionPredictor

# Load dataset
csv_file = "ethereum_data.csv"
dataset = BlockchainDataset(csv_file)
dataset = preprocess_data(dataset)
dataloader = create_dataloader(dataset)

# Initialize model, optimizer, and loss function
model = TransactionPredictor(input_dim=4)  # from_address, to_address, gas, gas_price
optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = MSELoss()

# Training loop
for epoch in range(10):
    for batch in dataloader:
        features, labels = batch
        from_address = features['from_address'].float()
        to_address = features['to_address'].float()
        gas = features['gas'].float()
        gas_price = features['gas_price'].float()

        inputs = torch.stack([from_address, to_address, gas, gas_price], dim=1)
        labels = labels.float()

        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs.squeeze(), labels)
        loss.backward()
        optimizer.step()

    print(f"Epoch {epoch + 1}, Loss: {loss.item():.4f}")

# sankey.py
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.sankey import Sankey

def create_sankey(csv_file):
    data = pd.read_csv(csv_file)

    sankey = Sankey()
    for _, row in data.iterrows():
        sankey.add(flows=[-row['value'], row['value']],
                   labels=[row['from_address'], row['to_address']],
                   orientations=[-1, 1])
    sankey.finish()
    plt.title('Blockchain Transactions Sankey Diagram')
    plt.show()

if __name__ == "__main__":
    create_sankey("ethereum_data.csv")
