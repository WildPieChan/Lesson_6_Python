# Specify a list of n numbers in the sequence
# (1 + 1 / n)**n and display their sum on the screen

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

def SumOfNumbersInTheSequence(resultList):
    result = []
    for i in range(len(resultList)):
        # result.appen(reduce(lambda x, y: round(x + y, 0), resultList)) - если округлять сразу, то финальный результат получается меньше необходимого
        result.append(reduce(lambda x, y: x + y, resultList))
        resultList.pop(len(resultList) - 1)
    return list(reversed(result))
    # return list(map(int, (reversed(result)))) - тоже рабочий вариант, однако при такой конвертациии результат получается меньше необходимого

n = InputNumber("Enter any integer number: ")
allNumbers = list(map(float, [x for x in range(1, n + 1)]))

result = list(map(lambda x: (1 + 1 / x)**x, allNumbers))
result = SumOfNumbersInTheSequence(result)
result = list(map(lambda x: round(float(x), 0), result))
result = map(int, result)
print(list(enumerate(result)))