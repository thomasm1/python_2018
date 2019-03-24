# From: Parallelism in one line: A Better Model for Day to Day Threading Tasks.
# 3.6 / win os

from multiprocessing.dummy import Pool as ThreadPool 
my_array = ['a', 'b', 'c', 'd']
def my_function(x):
    x = x*10
    print(x)
pool = ThreadPool(4) 
results = pool.map(my_function, my_array)

# the multithreaded version of:
my_array = ['a', 'b', 'c', 'd']
results = []
for item in my_array:
    results.append(my_function(item))
