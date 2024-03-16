from Users import user
from card import Card

Alex = user('Alex')
Petya = user('Petya')
Maria = user('Maria')

Alex.sayName()
Alex.setAge(input('Скок лет? '))
Alex.sayAge()

card = Card("4276 0821 6875 3801", '06/25', 'Alex P')
Alex.addCard(card)
Alex.getCard().pay(550900)