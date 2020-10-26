raw = int(input("How many raws of chocolate? ... "))
colum = int(input("How many colums of chocolate? ... "))
k = int(input("Enter the number to devide? ... "))

if (raw/k == raw//k) or (colum/k == colum//k):
    print("Possible to devide")
else:
    print("Impossible to devide")