%matplotlib inline
%config InlineBackend.figure_format = 'retina'

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb
sb.set_context("notebook", font_scale=1.25)

data - pd.read_csv('Users/tm/Data/fat.dat.txt', delim_whitespace=True, header=None)
data.columns = [case', 'density', 'age','weight']
data.index = data['case']
data = data.drop(['case'], axis=1)
data = data[data]['weight']<300]

data.head()
sb.pairplot(data[['weight','age']], size=2, plot_kws=('s':15, 'edgecolor':'non','alpha':0.7})
