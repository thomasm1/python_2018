
# todo: populate "squares" with the set of all of the integers less 
# than 2000 that are square numbers
squares = set()

def nearest_square(limit):
    answer = 0
    while (answer+1)**2 < limit:
        answer += 1
    return answer**2
lim = 2000
for c in range(lim):
    c += 1
    squares.add(nearest_square(c))
print(len(squares))
print(squares)

# Note: If you want to call the nearest_square function, you must define
# the function on a line before you call it. Feel free to move this code up!
