import random
"""
def walker_one(n):
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['n','s','e','w'])
        if step =='n':
            y = y+1
        elif step == 's':
            y = y-1
        elif step == 'e':
            x = x+1
        else:
            x = x-1
    return (x,y)

for i in range(24):
    walk = walker_one(10)
    print(walk, "distance from home ....",
        abs(walk[0]) + abs(walk[1]))
"""

def data_walker(n):
    x, y = 0, 0
    for i in range(n):
        # directionals
        (dx, dy) = random.choice([(0,1), (0,-1), (1,0),(-1,0)])
        x += dx
        y += dy
    return (x,y)
  #  num_of_walkers = 100
  #  for walk_length in range(1,31):
  
for i in range(24):
    walk = data_walker(10)
    print(walk, "distance from home ....",  abs(walk[0]) + abs(walk[1]))