if __name__ == '__main__':
    n = int(input().strip())
    if (n%2 != 0) or ((n%2 == 0) and (n in range(6,21))):
        print("Weird")
    else:
        print("Not Weird")
