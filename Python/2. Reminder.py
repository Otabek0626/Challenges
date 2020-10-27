a = int(input("Enter the A number... "))
b = int(input("Enter the B number... "))

n = int(input("Enter the N number... "))
counter = 0
for i in range(a,b):
    if i%n == 0:
        counter += 1
    else:
        continue
print(f'The number of devisions are {counter} without reminder')