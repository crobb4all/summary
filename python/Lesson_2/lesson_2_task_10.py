# 2. Дано: пользователь делает вклад в размере Х рублей сроком на Y лет под 10% годовых 
# (каждый год размер его вклада увеличивается на 10%, эти деньги прибавляются к сумме вклада, 
# и на них в следующем году тоже будут проценты).

# 3. Задача: написать функцию bank, принимающую аргументы X и Y и возвращающую сумму, 
# которая будет на счету пользователя спустя Y лет.

def bank(x, y):
    pros = 0.10
    A = x * (1 + pros) ** y
    return A

x = int(input('Add sum: '))
y = int(input('add year: '))
final_amount = bank(x, y)
print("Конечная сумма вклада через", y, "лет:", final_amount)
