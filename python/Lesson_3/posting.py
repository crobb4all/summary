from adress import Adress

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def print_mailing_info(self):
        print(f"Отправление {self.track} \nИЗ {self.from_address.adr_index}, {self.from_address.adr_city}, {self.from_address.adr_street}, д.{self.from_address.adr_house} - кв.{self.from_address.adr_room} \nВ {self.to_address.adr_index}, {self.to_address.adr_city}, {self.to_address.adr_street}, д.{self.to_address.adr_house} - кв.{self.to_address.adr_room}. \nСтоимость {self.cost} рублей.")
    