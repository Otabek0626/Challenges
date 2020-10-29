class helps:
    def Add_item():
        key = input("Enter a key: ")
        value = input("Enter a value: ")
        informations[key] = value
    def Delete_item():
        key = input("Enter a key: ")
        del informations[key]
    def Search_item():
        key = input("Enter a key: ")
        print(informations.get(key))
    def Show_all():
        for keys,values in informations.items():
            print(keys, ":", values)


informations = {}
while True:
    print('''=== Personal Contact List Management System ===
        1. Add
        2. Delete
        3. Search
        4. Show all
        5. Exit program''')
    select = int(input("Select a menu item: "))
    if select == 1:
        helps.Add_item()
    elif select == 2:
        helps.Delete_item()
    elif select == 3:
        helps.Search_item()
    elif select == 4:
        helps.Show_all()
    elif select == 5:
        break