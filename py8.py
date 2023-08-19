def myfun(n):
    return lambda :a * n
mydoubler=myfun(2)
print(mydoubler(11))
