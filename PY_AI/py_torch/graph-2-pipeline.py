import pandas as pd
import torch
from sklearn.preprocessing import LabelEncoder

#dataset load
df = pd.read_csv("blockchain_data.csv")

encoder = LabelEncoder()
df["Source"] = encoder.fit_transform(df["Source"])
df["Target"] = encoder.fit_transform(df["Target"])

sources = torch.tensor(df["Source"].values, dtype=torch.long)
targets = torch.tensor(df["Target"].values, dtype=torch.long)
values = torch.tensor(df["Value"].values, dtype=torch.float32)