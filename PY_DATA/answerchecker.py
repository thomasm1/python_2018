def check_answers(my_answers,answers,percent): 
    x = 0 
    count_correct = 0
    for i in my_answers: 
        if i == answers[x]:
            count_correct += 1
            x += 1  
        else:
            x += 1
    # here I pass forward # correct and sum #
    if  float(count_correct)/float(x)  > percent:
     #8 The pass rate has been hard-coded into the function
        print("Congratulations, you passed the test! You scored " + str(count_correct) + " out of " + str(x))
        return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of " + str(x)
 
    else:      
        print("Unfortunately, you did not pass. You scored " + str(count_correct) + " out of " + str(x))
        return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of " + str(x)
  

check_answers([3,3,3,3,3,3,4],[3,3,3,3,3,3,3],.75)
check_answers([3,2],[3,3],.75)  
check_answers([3,3],[3,3],.75)
check_answers([3,3,3,3,2],[3,3,3,3,3],.75)
check_answers([1,2,3,4,5],["badger","badger","badger","badger","badger"],.75)
check_answers([1,2,3,4,5],[1,2,3,4,5],.75)
