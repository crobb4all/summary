#right version
import math

def square(side):
    if isinstance(side, int) or side.is_integer():
        return side ** 2
    else:
        return math.ceil(side ** 2)

write = float(input("Введите сторону: "))
result = square(write)
print(result)

# #V.0.1
# def square(a):

#     y = a ** 2
#     print(y)

# square(4.5)

# #V.0.2
# def square():
#     a = int(input("Введите размер стороны: "))
#     y = a ** 2
#     print(y)

# square()