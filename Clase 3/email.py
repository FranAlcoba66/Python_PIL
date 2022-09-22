import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Z|a-z]{2,}\b'
value = input("Ingresar mail: ")

def check(a):

    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, a)):
        print("Valid Email")
        # next()
    else:
        print("Invalid Email")
        value2 =  input("Mal ingresado ,Reingresar mail: ")
        check(value2)

def recheck(a):

    if value==a:
        print("pillin")
        # next


check(value)

recheck(value)