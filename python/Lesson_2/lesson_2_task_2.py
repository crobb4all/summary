# Version 1
def is_year_leap():
    year = int(input("Введите год: "))
    y = year % 4
    print(f'год {year} : {y == 0}')

is_year_leap()

print('end point')

# Version 2
def is_year_leap(t):
    y = t % 4
    print('год', t,': ', y == 0)

is_year_leap(2024)

print('end point')