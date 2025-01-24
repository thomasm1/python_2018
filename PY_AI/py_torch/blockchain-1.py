# dataset.py
import pandas as pd
from torch.utils.data import Dataset

class BlockchainDataset(Dataset):
    def __init__(self, csv_file): 
        self.data = pd.read_csv(csv_file)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        row = self.data.iloc[idx]
        # Extract input features and labels (e.g., predict "Amount")
        features = {
            'sender': row['Sender'],
            'receiver': row['Receiver'],
            'fee': row['Transaction_Fee'],
        }
        label = row['Amount']
        return features, label
