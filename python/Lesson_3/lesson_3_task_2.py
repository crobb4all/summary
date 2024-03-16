from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 12", "+1234567890"),
    Smartphone("Samsung", "Galaxy S21", "+9876543210"),
    Smartphone("Xiaomi", "Redmi Note 10", "+1357924680"),
    Smartphone("Huawei", "P40 Pro", "+2468013579"),
    Smartphone("OnePlus", "8T", "+9876543210")
]

for phone in catalog:
    print(f"{phone.ph_brand} - {phone.ph_model} | {phone.ph_number}")
