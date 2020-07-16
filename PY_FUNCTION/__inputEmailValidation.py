import re
 

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
print("starting email check, use quotes around input")
def check(email):
    if re.search(regex,email):
    # if re.match(regex,emailadd,re.IGNORECASE):
        print("Valid email")
    else:
        print("Invalid email")

if __name__ == '__main__' :
    print("cli application...")
    email = input("Enter Email: ")
    check(email)
 
