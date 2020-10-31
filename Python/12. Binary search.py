def search(list, n):
    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (u+l) // 2

        if list[mid] == n:
            return True
        elif list[mid] < n:
            l = mid+1
        else:
            u = mid-1
    return False

list = [1, 4, 5, 7, 8, 12, 123, 1234]
n = 3

print(search(list, n))
