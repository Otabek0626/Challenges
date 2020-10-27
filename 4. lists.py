if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    data = []
    listofdata = []

    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                data.append(i)
                data.append(j)
                data.append(k)
                listofdata.append(data)
                data = []


    ans = []

    for s in listofdata:
        if sum(s) != n:
            ans.append(s)

    
    print(ans)

