# Write a program that takes the coordinates of two points as 
# input and finds the distance between them in 2D space.

print('Point A coordinate')
x1 = float(input('Enter X: '))
y1 = float(input('Enter Y: '))

print('Point B coordinate')
x2 = float(input('Enter X: '))
y2 = float(input('Enter Y: '))

power = lambda x: x**2
sqrt = lambda x: x**0.5
result = lambda a1, a2, b1, b2, fn_pow, fn_sqrt: fn_sqrt(fn_pow(a2 - a1) + fn_pow(b2 - b1))

print('Distance between two points A and B is {0:.2f}'.format(result(x1, x2, y1, y2, power, sqrt)))