def search(list, n):
    for i in list:
        if i == n:
            return True
    return False

list = [12, 32, 43, 543, 123, 42, 4 , 3]
n = 123

print(search(list, n))