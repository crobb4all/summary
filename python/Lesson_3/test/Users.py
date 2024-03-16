class user:
    age = 0;

    def __init__(self, name ):
        print('i am ready')
        self.username = name
    

    def sayName(self):
        print('my name is ', self.username)

    def sayAge(self):
        print(self.age)

    def setAge(self, newAge):
        self.age = newAge

    def addCard(self, card):
        self.card = card

    def getCard(self):
        return self.card