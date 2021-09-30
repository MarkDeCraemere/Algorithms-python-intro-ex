current = 1
previous = 2
sum = 1

while current < 4000000:
    nextNumber = previous + current

    if nextNumber % 2 != 0:
        sum += nextNumber

    previous = current
    current = nextNumber
    

print(sum)