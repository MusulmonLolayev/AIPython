# Bo'sh Lug'at yaratish
phonenumbers_dict  = {}

# Func adding new number
def AddNumber():
    # Calling phonenumbers_dict for local
    global phonenumbers_dict

    # Creat new phone number
    newPhone = {input("Enter new phone number: ") : {
        "fio" : {
            "fam" : input("Enter last name: "),
            "ism" : input("Enter first name: "),
            "middle" : input("Enter midle name: ")
        },
        "address" : {
            "place" : input("Enter address: "),
            "email" : input("Enter e-mail: ")
        }
    }}

    # Adding the number note the new number
    phonenumbers_dict.update(newPhone)

# Func: deleting the needed number
def DeleteNumber():
    # Calling phonenumbers_dict for local
    global phonenumbers_dict
    # Input the numbers data for deleting
    pass

# Func: Editing the needed number
def EditNumber():
    # Calling phonenumbers_dict for local
    global phonenumbers_dict
    # Input the numbers data for deleting
    pass

# Func: Editing the needed number
def PrintNumbers():
    # Calling phonenumbers_dict for local
    global phonenumbers_dict

    for item in phonenumbers_dict:
        print("Phone number: ", item)
        print("" * 20, end='')
        print("F.I.O.: ", item["fio"]["fam"],
              " | ", item["fio"]["ism"], " | ",
              item["fio"]["midle"])
        print("Address: ", item["address"]["place"],
              " | ", item["address"]["email"])

def SearchByFirstName():
    # Calling phonenumbers_dict for local
    global phonenumbers_dict

def SearchByAddress():
    # Calling phonenumbers_dict for local
    global phonenumbers_dict

while True:
    print("Buyruqlar:")
    print("1-Yangi raqam qo'shish")
    print("2-Tarirlash")
    print("3-O'chirish")
    print("4-Chop qilish")
    print("5-Familiya bo'yicha qidirish")
    print("6-Manzil bo'yicha qidirish")
    print("0-Chiqish")

    # Buyruqni kiritish
    command = int(input("Buyruq raqamini kiriting: "))
    # Birinchi buyroq funksiyasiga murojat qilish
    if command == 1:
        AddNumber()
        # Keyingi if shartlarni qaramaslik uchun
        continue

    # 2-buyroq funksiyasiga murojat qilish
    if command == 2:
        EditNumber()
        continue

    # 3-buyroq funksiyasiga murojat qilish
    if command == 3:
        DeleteNumber()
        continue
    # 4-buyroq funksiyasiga murojat qilish
    if command == 4:
        continue
    # 5-buyroq funksiyasiga murojat qilish
    if command == 5:
        SearchByFirstName()
        continue
    # 6-buyroq funksiyasiga murojat qilish
    if command == 6:
        SearchByAddress()
        continue
    # 0-buyroq funksiyasiga murojat qilish
    if command == 0:
        # Exit while
        break