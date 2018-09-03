def median(numbers):
    numbers.sort() #The sort method sorts  list directly, rather than returning a new sorted list
    if (int(len(numbers))% 2)==0:
        middle_index = int(len(numbers)/2)
        middle2_index = int(len(numbers)/2)-1
        return float((numbers[middle_index]+numbers[middle2_index])/2) 
    else:
        middle_index = int(len(numbers)/2)
        return numbers[middle_index]

test1 = median([1,2,3])
print("expected result: 2, actual result: {}".format(test1))

test2 = median([1,2,3,4])
print("expected result: 2.5, actual result: {}".format(test2))

test3 = median([53, 12, 65, 7, 420, 317, 88])
print("expected result: 65, actual result: {}".format(test3))

test4 = median([77, 53, 12, 65, 7, 420, 317, 88])
print("expected result: 65, actual result: {}".format(test4))


