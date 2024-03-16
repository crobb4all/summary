class User:
    def __init__(self, first_name, last_name):
        self.FN = first_name
        self.LN = last_name
        
    def sayFirstN(self):
        print('Имя: ', self.FN)

    def sayLastN(self):
        print('Фамилия: ', self.LN)

    def sayFullName(self):
        print('Полное имя: ', self.FN, self.LN)



    #   def sayName(self):
    #     print('my name is ', self.username)      