# michael.lensi@ruralsourcing.com

from inveetro2 import *
import math
import sys
import webbrowser

num_chrom_per_gen = 50
num_generations = 100

pool = param_pool()

SELECT_PROBLEM = 2

if SELECT_PROBLEM is 1:
    
    pool.add_param(ga_param(-50, 50, 1))
    pool.add_param(ga_param(-40, 60, .5))

    webstr = "https://academo.org/demos/3d-surface-plotter/?expression=6000-abs(x*x%2By*y)&xRange=-50%2C+50&yRange=-40%2C+60&resolution=34"
    fit = lambda s: 6000.0 - abs(s[0]**2 + s[1]**2)

    opt_soln = [0, 0]
    
elif SELECT_PROBLEM is 2:
    
    pool.add_param(ga_param(-3, 3, .1))
    pool.add_param(ga_param(-3, 3, .01))

    webstr = "https://academo.org/demos/3d-surface-plotter/?expression=3*(1-x)%5E2*exp(-(x%5E2)-(y%2B1)%5E2)-10*(x%2F5-x%5E3-y%5E5)*exp(-x%5E2-y%5E2)-1%2F3*exp(-(x%2B1)%5E2-y%5E2)&xRange=-3%2C%2B3&yRange=-3%2C%2B3&resolution=34"
    fit = lambda s: 3*(1-s[0])**2*math.exp(-(s[0]**2) - (s[1]+1)**2) - 10*(s[0]/5 - s[0]**3 - s[1]**5)*math.exp(-s[0]**2-s[1]**2) - 1/3*math.exp(-(s[0]+1)**2 - s[1]**2)
    
    opt_soln = [0, 1.58]
    
else:
    print("Setup your problem properly why don't ya.")
    sys.exit()

web_fit = lambda: webbrowser.open(webstr)

stats = {
    "target": fit(opt_soln),
    "gen": None,
    "solspace": 0,
    "tested": 0,
    "percent": 0
}
solspace = 1.0
for ga_param in pool.pool:
    solspace *= (ga_param.pF - ga_param.p0) / ga_param.pD
stats["solspace"] = solspace


G = init_generation(pool, num_chrom_per_gen)

fitnesses = eval_fitnesses(pool, fit, G)

newG = new_generation(G, fitnesses)

for i in range(num_generations):
    print( "\n------- GENERATION {0} -------".format(i) )
    fitnesses = eval_fitnesses(pool, fit, newG)
    
    if stats["target"] in fitnesses and stats["gen"] is None:
        stats["gen"] = i
    
    G = newG[:]
    newG = new_generation(G, fitnesses)  #, 0.25, 0.05)

    best = newG[0]
    best_dec = pool.solution_to_decimal(newG[0])

    print( "\nHighest fitness = {0}".format(fit(best_dec)) )
    print( "\nBest solution (binary) = {0}".format(best) )
    print( "\nBest solution (decimal) = {0}".format(best_dec) )


if stats["gen"] is not None:
    stats["tested"] = stats["gen"] * num_chrom_per_gen
    stats["percent"] = stats["tested"] / stats["solspace"] * 100

print( "\nRun Statistics:" )
for key, value in stats.items():
    print(f"{key} = {value}")

