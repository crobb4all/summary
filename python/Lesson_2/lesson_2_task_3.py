#Ver. 2.0
import math

def square(side):
    if isinstance(side, int) or side.is_integer():
        return side ** 2
    else:
        return math.ceil(side ** 2)

write = float(input("Введите сторону: "))
result = square(write)
print(result)

#Ver. 1.0
def square(side):
    if isinstance(side, int) or side.is_integer():
        return side ** 2
    else:
        return math.ceil(side ** 2)

print(square(float(input('Введите сторону: '))))