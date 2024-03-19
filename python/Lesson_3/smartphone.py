class Smartphone:

    def __init__(self, phone_brand, phone_model, phone_number):
        self.ph_brand = phone_brand
        self.ph_model = phone_model
        self.ph_number = phone_number

    def sayBrand(self):
        print("Брэнд телефона: ", self.ph_brand)

    def sayModel(self):
        print('Модель: ', self.ph_model)

    def sayNumber(self):
        print('Номер телефона: +7', self.ph_number)
