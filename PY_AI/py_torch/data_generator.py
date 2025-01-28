import pandas as pd

# Mock data for blockchain transactions
data = {
    "Transaction_ID": [f"tx_{i}" for i in range(1, 11)],
    "Timestamp": [
        "2025-01-22 10:00:00", "2025-01-22 10:05:00", "2025-01-22 10:10:00",
        "2025-01-22 10:15:00", "2025-01-22 10:20:00", "2025-01-22 10:25:00",
        "2025-01-22 10:30:00", "2025-01-22 10:35:00", "2025-01-22 10:40:00",
        "2025-01-22 10:45:00"
    ],
    "Sender": [f"wallet_{i}" for i in range(1, 11)],
    "Receiver": [f"wallet_{i+10}" for i in range(1, 11)],
    "Amount": [100, 250, 300, 150, 200, 350, 400, 50, 75, 125],
    "Transaction_Fee": [0.01, 0.015, 0.02, 0.01, 0.025, 0.02, 0.03, 0.01, 0.015, 0.02]
}

# Create a DataFrame
blockchain_df = pd.DataFrame(data)

# Save to a CSV file
file_path = "/mnt/data/blockchain_data.csv"
blockchain_df.to_csv(file_path, index=False)
file_path
