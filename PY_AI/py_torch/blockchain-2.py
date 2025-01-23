# pipeline.py
import torch
from torch.utils.data import DataLoader
from sklearn.preprocessing import LabelEncoder

def preprocess_data(dataset):
    # Encode sender and receiver addresses as integers
    sender_encoder = LabelEncoder()
    receiver_encoder = LabelEncoder()

    dataset.data['Sender'] = sender_encoder.fit_transform(dataset.data['Sender'])
    dataset.data['Receiver'] = receiver_encoder.fit_transform(dataset.data['Receiver'])

    return dataset

def create_dataloader(dataset, batch_size=2):
    return DataLoader(dataset, batch_size=batch_size, shuffle=True)