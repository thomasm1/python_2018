# Price One to 3x + 1
def fn(x):
    return 3*x + 1 
fn(2)
print("1: ", fn(2))
#/
g = lambda x: 3*x + 1
print("lambda: ", g(2))

coin_owner = lambda g, ln: g.strip().title() + " " + ln.strip().title()
print(coin_owner(" thomas", "MaesTAS"))

lambda : "what is the coin price?"
lambda x: 3*x+1 
lambda x, y: (x*y)**0.5 # Geometric mean
lambda x, y, z: 3/(1/y + 1/z) # Harmonic mean

all_coin_owners = ["henry ford", "tom Maestas", "William F. BUckley", "fname, mname, lname"]
help(all_coin_owners.sort)

names = all_coin_owners.sort(key=lambda name: name.split(" ")[-1].lower())
print(names)
