#TODO: Implement the nearest_square function
def nearest_square(limit):
    r = 0
    ans = 0
    while ans <= limit: 
        ans = r*r
        if ans > limit:
            break 
        r += 1
        a = ans
    return a 
test1 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test1))
def nearest_square(limit):
    answer = 0
    while (answer+1)**2 < limit:
        answer += 1
    return answer**2
test2 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test2))
