# For BitcoinBuyer program tools:
# Thomas Maestas
# Source: meetup August 5, 2019
# Program to demo Eratosthene's Sieve
# Verbose to demonstrate loops and function calls

import time

t1 = time.perf_counter()
print('Begin timing time.perf_counter()...', t1)
# 4th block to run. Called by the loop below with different
# factors until the set of factors is exhausted
def create_multiples(factor, limit):
    """Return a set of multiples of the factor up to the limit.
    Start with factor**2."""
    multiples = set()
    counter = 0
    product = 0

    print('    Function begins.')
    while True:
        product = factor * (factor + counter)
        if product > limit:
            print(f'    {factor} * {factor + counter} = {product}.',
                  f'Loop within function breaks. Fucntion returns ouput')
            break
        multiples.add(product)
        print(f'    {factor} * {factor + counter} = {product}')
        counter += 1
        print('Multiples: ' )
    return multiples
print('1st block: Declaring vars, creating the sets ...')
print('0.) ...Initializing variables:')
limit = 100
square_root = int(limit**.5)
print('1.) square_root int(%d **.5: %d)' % (limit, square_root))
print()
integers = {i for i in range(2, limit + 1)}
print('2.) integers = {i for i in range(2, limit + 1)}:')
print(integers)
print()
potential_factors = {i for i in range(2, square_root + 1)}
print('3.) potential_factors = {i for i in range(2, square_root + 1)}:')
print(potential_factors)
print()
t2 = time.perf_counter()
print('After second block ...  ', t2)
t_elapse1 = (t2 - t1)
print('Time2 - Time1, elapsed: ', t_elapse1)

