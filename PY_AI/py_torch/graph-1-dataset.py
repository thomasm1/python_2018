import pandas as pd

#synthetic blockchain 
data = {
    "Source": ["WalletA", "WalletB", "WalletA", "WalletC"],
    "Target": ["WalletB", "WalletC", "WalletD", "WalletD"],
    "Value": [100, 150, 200, 50]
}

df = pd.DataFrame(data)
df.to_csv("blockchain_data.csv", index=False)
print("dataset created as blockchain_data.csv")
