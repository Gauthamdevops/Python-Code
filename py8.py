# Lambda Function in Python

def myfun(n):
    return lambda a : a * n
mydoubler=myfun(2)
print(mydoubler(11))
