def sumInRangeDivBySevenAndNine(x):
    sum = 0
    for i in range(0, x):
        if i % 7 == 0 or i % 9 == 0:
            sum += i
    return sum

print(sumInRangeDivBySevenAndNine(10000))

