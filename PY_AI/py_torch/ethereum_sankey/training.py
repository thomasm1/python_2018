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