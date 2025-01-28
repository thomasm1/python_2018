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