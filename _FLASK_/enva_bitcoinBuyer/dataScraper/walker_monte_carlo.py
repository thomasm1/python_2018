import random

def data_walker(n):
    x, y = 0, 0
    for i in range(n):
        # directionals
        (dx, dy) = random.choice([(0,1), (0,-1), (1,0),(-1,0)])
        x += dx
        y += dy
    return (x,y)

num_of_walkers = 1000
for walk_length in range(1,31):
    no_transport = 0
    for i in range(num_of_walkers):
        (x,y) = data_walker(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
          no_transport += 1
    no_transport_percent = float(no_transport)/ num_of_walkers
    print("walk length = ", walk_length, "/% of no transport = ", 100*no_transport_percent)


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
