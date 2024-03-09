# #Version 1
def month_to_season(m_n):
    if m_n == 12 or m_n == 1 or m_n == 2:
        print('Зима')
    elif m_n >= 3 and m_n <= 5:
        print('Весна')
    elif m_n >= 6 and m_n <= 8:
        print('Лето')
    elif m_n >= 9 and m_n <= 11:
        print('Осень')
    else:
       print('Такого месяца нет')

month_to_season(5)

#Version 2
# def month_to_season(month):
#     seasons = {
#         1: "Зима",
#         2: "Зима",
#         3: "Весна",
#         4: "Весна",
#         5: "Весна",
#         6: "Лето",
#         7: "Лето",
#         8: "Лето",
#         9: "Осень",
#         10: "Осень",
#         11: "Осень",
#         12: "Зима"
#     }
#     return seasons.get(month, "Некорректный месяц")

# month = 6
# print("Месяц", month, "cезон:", month_to_season(month))
