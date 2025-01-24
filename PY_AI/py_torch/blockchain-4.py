# training.py
import torch
import torch.optim as optim
from torch.nn import MSELoss
from dataset import BlockchainDataset
from pipeline import preprocess_data, create_dataloader
from model import TransactionPredictor
 
csv_file = "blockchain_data.csv"
dataset = BlockchainDataset(csv_file)
dataset = preprocess_data(dataset)
dataloader = create_dataloader(dataset)

# Initialize model, optimizer, and loss function
model = TransactionPredictor(input_dim=3)  # sender, receiver, fee
optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = MSELoss()

# Training loop
for epoch in range(10):
    for batch in dataloader:
        features, labels = batch
        sender = features['sender'].float()
        receiver = features['receiver'].float()
        fee = features['fee'].float()

        inputs = torch.stack([sender, receiver, fee], dim=1)
        labels = labels.float()

        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs.squeeze(), labels)
        loss.backward()
        optimizer.step()

    print(f"Epoch {epoch + 1}, Loss: {loss.item():.4f}")