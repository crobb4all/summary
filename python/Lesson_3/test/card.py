class Card:
    number = '0000 0000 0000 0000'
    endDate = '12/25'
    holder = 'unknown'

    def __init__(self, number, date , holder):
        self.number = number
        self.endDate = date
        self.holder = holder


    def pay(self, amound):
        print('С карты: ', self.number, '\nСписано: ', amound, 'рублей')


