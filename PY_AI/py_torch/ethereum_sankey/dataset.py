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