file_name = r"table.txt"

# Func adding new number
def AddNumber():
    # Calling file_name for local
    global file_name
    with open(file_name, 'a') as table:
        fam = input("Familiya: ")
        ism = input("Ism: ")
        yosh = int(input("Yosh: "))
        kurs = int(input("Kurs: "))
        average = float(input("O'rtacha baho: "))

        print(fam, "\t", ism, "\t", yosh, "\t", kurs, "\t", average, file=table)

# Func: deleting the needed number
def DeleteNumber():
    # Calling file_name for local
    global file_name
    pass

# Func: Editing the needed number
def EditNumber():
    # Calling file_name for local
    global file_name
    pass

# Func: Editing the needed number
def PrintNumbers():
    # Calling file_name for local
    global file_name

    with open(file_name, 'r') as table:
        for line in table:
            print(line)

def SearchByFirstName():
    # Calling phonenumbers_dict for local
    global phonenumbers_dict
    s = input("Enter any text: ")

    with open(file_name, 'r') as table:
        for line in table:
            fam = line.split("\t")[0]
            if s in fam:
                print(line)

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