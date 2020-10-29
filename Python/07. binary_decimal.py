def Decimal_to_Binary():
    number = int(input("Decimal to Binary: "))
    binary = ""
    while number * 2 > 1:
        binary += str(number % 2)
        number = number // 2
    print(binary[::-1])
def Binary_to_Decimal():
    number = str(input("Binary to Decimal: "))
    number = number[::-1]
    length = len(number)
    result, i = 0, 0
    while length > 0:
        result += int(number[i]) * (2 ** i)
        i += 1
        length -= 1
    print(result)
while True:
    input("Click the enter to start... ")
    choose = input('''DtB for "Decimal to Binary"
BtD for "Binary to Decimal"
Exit for close the window
Enter... ''')
    choose = choose.lower()
    if choose == "dtb":
        Decimal_to_Binary()
    elif choose == "btd":
        Binary_to_Decimal()
    elif choose == "exit":
        exit()
    else:
        print("Your choise is invalid please check again!!!")