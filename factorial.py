def calcFunc(numF):
    factorial = 1
    while numF > 1:
        factorial *= numF
        numF -= 1
    return factorial

numF = 5
factorial = calcFunc(numF)
print("The factorial of %d is %d" % (numF, factorial))

