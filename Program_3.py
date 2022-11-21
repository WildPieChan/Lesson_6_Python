# Write a program that accepts the number N as input and
# outputs a set of multiplication of number from 1 to N.

from functools import reduce

def InputNumber(inputText):
    ok = False
    while not ok:
        try:
            number = int(input(f"{inputText}"))
            ok = True
        except ValueError:
            print("Error. Only integer numbers. Try again...")
    return number

def MultiplicationFromOneToN(allNumbers):
    result = []
    for i in range(len(allNumbers)):
        result.append(reduce(lambda x, y: x * y, allNumbers))
        allNumbers.pop(len(allNumbers) - 1)
    return list(reversed(result))

n = InputNumber("Enter any integer number: ")
allNumbers = list(map(int, [x for x in range(1, n + 1)]))
result = MultiplicationFromOneToN(allNumbers)
print(result)