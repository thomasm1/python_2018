# sankey.py
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.sankey import Sankey

def create_sankey(csv_file):
    data = pd.read_csv(csv_file)

    sankey = Sankey()
    for _, row in data.iterrows():
        sankey.add(flows=[-row['Amount'], row['Amount']],
                   labels=[row['Sender'], row['Receiver']],
                   orientations=[-1, 1])
    sankey.finish()
    plt.title('Blockchain Transactions Sankey')
    plt.show()

if __name__ == "__main__":
    create_sankey("blockchain_data.csv")