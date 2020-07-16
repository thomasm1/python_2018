# BitcoinBuyer program tools:
# Thomas Maestas
# Pandas Seaborn Vector iterator
# using baseline of 0) loop and 1) generator itterrows()
# 3) .apply() lambda fx using cython iterators
# 4) .cut() pandas function takes as input a set of bins defining each range of if/else
#      and a  set of labels, similar to std for-loop

import time
import seaborn as sns
import pandas as pd
data = sns.load_dataset('iris') 
print(data.head())
print()

#0 Traditional For-loop time performance:
data = sns.load_dataset('iris')
def find_class(petal_length):
    if petal_length <= 2:
        return 1
    elif 2 < petal_length < 5:
        return 2
    else:
        return 3

start = time.time()
time1 = time.perf_counter() 

class_list = list()
for i in range(len(data)):
    petal_length = data.iloc[i]['petal_length']
    class_num = find_class(petal_length)
    class_list.append(class_num)

end = time.time()
print('STD FOR-LOOP run time = {}'.format(end - start)) # 0.03088
print('time1: ', time1)
print()

#1 For-loop with Pandas .iterrows()
data = sns.load_dataset('iris')
def find_class(petal_length):
    if petal_length <= 2:
        return 1
    elif 2 < petal_length < 5:
        return 2
    else:
        return 3

start = time.time()  
time2 = time.perf_counter() 

class_list = list()
for index, data_row in data.iterrows():
    petal_length = data_row['petal_length']
    class_num = find_class(petal_length)
    class_list.append(class_num)

end = time.time()
print('ITERROWS() FOR-LOOP run time = {}'.format(end - start)) # 0.01792
print('time2: ', time2)
print()

#2 Vector calculation using .apply()
data = sns.load_dataset('iris')
def find_class(petal_length):
    if petal_length <= 2:
        return 1
    elif 2 < petal_length < 5:
        return 2
    else:
        return 3

start = time.time() 
time3 = time.perf_counter() 
class_list = list()
class_list = data.apply(lambda row: find_class(row['petal_length']), axis=1)

end = time.time()
print('.apply() run time = {}'.format(end - start)) # 0.00935
print('time3: ', time3)
print()


#3 Vector calculation using .cut() (Cython)
data = sns.load_dataset('iris')
start = time.time() 
timeEnd = time.perf_counter() 

class_list = pd.cut(x=data.petal_length,
                    bins=[0,2,5,100],
                    include_lowest=True,
                    labels=[1,2,3]).astype(int)
end = time.time()
print('.cut() run time = {}'.format(end - start)) # 0.00790
print('timeEnd: ', timeEnd)
print()


  
