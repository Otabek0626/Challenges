if __name__ == '__main__':
    dataset = []
    for i in range(int(input())):
        data = []
        data.append(input())
        data.append(float(input()))
        dataset.append(data)
    scores = []
    for i in dataset:
        scores.append(i[1])
    
    
    z = min(scores)
    while z == min(scores):
        scores.remove(z)
    z = min(scores)

    ans = []
    for i in dataset:
        if i[1] == z:
            ans.append(i[0])
    z = sorted(ans)
    for i in z:
        print(i)
