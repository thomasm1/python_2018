
# coding: utf-8

# In[2]:
import pandas as pd
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks.dtypes

# In[5]: 
import numpy as np
drinks.select_dtypes(include=[np.number]).dtypes
# In[6]:
 
drinks.describe()

drinks.describe(include='all')
 

drinks.describe(include=['object'])
 
drinks.head()

 
drinks.drop('continent', axis=1).head()

 drinks.drop(2, axis=0).head()

 drinks.mean(axis=0)

 drinks.mean(axis=1)
 

drinks.drop(2, axis=0).head()
 
drinks.mean(axis=1).shape

 
drinks.mean(axis='columns')

 

drinks.country.str.upper()

 

drinks[drinks.country.str.contains('Vietnam')]
 

drinks[drinks.country.str.startswith('U')]
 


drinks.country.str.replace(' ', '_').str.replace('\'','')
 


drinks.dtypes
 
drinks.beer_servings.astype(float)
 
drinks_float = pd.read_csv('http://bit.ly/drinksbycountry', dtype={'beer_servings':float})
drinks_float.dtypes
 
drinks_float.wine_servings.mean()
 
drinks_float.wine_servings.astype(int).mean()


# In[39]:


drinks_float.wine_servings.astype(float).mean()

drinks_float.groupby('continent').wine_servings.mean()


drinks_float[drinks_float.continent=='North America'].wine_servings.mean()

drinks_float[drinks_float.continent=='Europe'].wine_servings.mean()

drinks_float.groupby('continent').wine_servings.max()

drinks_float.groupby('continent').wine_servings.agg(['count','min','max','mean'])

drinks_float.groupby('continent').mean()

get_ipython().magic('matplotlib inline')

drinks.groupby('continent').mean().plot(kind='bar')


drinks.continent.value_counts()

drinks.continent.value_counts(normalize=True)

pd.crosstab(drinks.country,drinks.continent).head()
 

get_ipython().magic('matplotlib inline')

drinks.continent.value_counts().plot(kind='bar')

drinks.groupby('continent').mean().plot(kind='bar')

drinks.dtypes

drinks.isnull().sum()

drinks[drinks.continent.isnull()]

drinks.shape

drinks.dropna(how='any').shape

drinks.dropna(subset=['country', 'continent'], how='all').shape

drinks['continent'].value_counts(dropna=False)

drinks['continent'].fillna(value='MISCELLANEOUS', inplace=True)

drinks.loc[0,:]

drinks.loc[[0,1,2],:]


drinks.loc[:,'beer_servings':'wine_servings'].head(10)


drinks.head(5).drop('total_litres_of_pure_alcohol', axis=1)


drinks.columns


list(range(0,4))

drinks.iloc[:,0:4].tail(10)

