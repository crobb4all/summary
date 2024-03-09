def bank(x, y):
    pros = 0.10
    a = round(x * (1 + pros) ** y, 2)
    return a

x = int(input('Add sum: '))
y = int(input('add year: '))
final_amount = bank(x, y)
print("Конечная сумма вклада через", y, "лет:", final_amount)
