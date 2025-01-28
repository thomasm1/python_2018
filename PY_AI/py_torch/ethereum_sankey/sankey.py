import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.sankey import Sankey

def create_sankey(csv_file):
    data = pd.read_csv(csv_file)

    sankey = Sankey()
    for _, row in data.iterrows():
        sankey.add(flows=[-row['value'], row['value']],
                   labels=[row['from_address'], row['to_address']],
                   orientations=[-1, 1])
    sankey.finish()
    plt.title('Blockchain Transactions Sankey Diagram')
    plt.show()

if __name__ == "__main__":
    create_sankey("ethereum_data.csv")