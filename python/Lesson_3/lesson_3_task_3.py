from adress import Adress
from posting import Mailing


to_address = Adress('100345', 'Москва', 'Маяковского', '12', '56')
from_address = Adress('6002', 'Signakhi', 'Djavahishvili', '54', '87')

mailing = Mailing(to_address, from_address, 500, "RL12495073HL")

mailing.print_mailing_info()