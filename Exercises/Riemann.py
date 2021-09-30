import math

def f(x):
    return math.pow(x, 2) + 3 * x + 15

def riemannIntegral(interval, a):
    x = interval[0]
    step = (interval[1] - interval[0]) / a
    x1 = x + step

    integral = 0

    for i in range (interval[0], a):
        width = x1 - x
        height = f(x1)
        integral += width * height

        x = x1
        x1 = x + step

    return integral

print(riemannIntegral([0, 5], 5))
print(riemannIntegral([0, 5], 8))
print(riemannIntegral([0, 5], 1_000_000))