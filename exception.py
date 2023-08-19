import random
num=random.randint(1,10)
class Error(Exception):
    pass
class ValueSmallError(Error):
    pass
class ValueLargeError(Error):
    pass
while(True):
    try:
        guess=int(input("enter a number: "))
        if guess<num:
            raise ValueSmallError
        elif guess>num:
            raise ValueLargeError
        break
    except ValueSmallError:
        print("this is small,, Try again!!!!!!!")
    except ValueLargeError:
        print("This is Large, Ty Again!!!!!!!!!!!!!!!!")
print("Congrats!!!!!! You Guessed it correctly.............................")
                
