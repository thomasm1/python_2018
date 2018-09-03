def check_answers(my_answers,answers):
    #1 variable names are not easy to tell apart
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    """
    #2 Code will only work if there are exactly five answers
    results= [None, None, None, None, None]
    #3 Repeated code would be better as a separate function
    count_correct = 0
    count_incorrect = 0
    for i in my_answers:
        if i == answers[i]:
            results[i] = True
        else:
            results[i] = False
    for result in results:
        #7 The code counts both correct and incorrect answers.
        if result == True:
            count_correct += 1
        if result != True:
            count_incorrect += 1
        if count_correct/5 > 0.7:
        #8 The pass rate has been hard-coded into the function
            return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
            print("Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5.")
        elif count_incorrect/5 >= 0.3:
            return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."
            print("Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5.")
check_answers([3,3,3,3,3],[3,3,3,3,3])
