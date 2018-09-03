#matplotlib
from matplotlib import rcsetup
rcsetup.all_backends

import matplotlib.pyplot as plt
import pandas as pd
iris = pd.read_csv('iris.csv')
iris.head()
color_map = dict(zip(iris.species.unique(),['blue','green','red']))

for species, group in iris.groupby('species'):
    plt.scatter(group['petal_length'], group['sepal_length'],
                color=color_map[species],
                alpha=0.3, edgecolor=None,
                label=species)

plt.legend(frameon=True, title='species')
plt.xlabel('petalLength')
plt.ylabel('sepalLength')

