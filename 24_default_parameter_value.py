

'''    Default parameter value:
        * we can have a value as default argument in a function.
        * if we specify name = 'stranger' in the line containing def,
                   this value is used when no argument is passed.
'''



def greet(name = 'stranger'):
    print("Good evening, "+name)

greet("Harshal")
greet()