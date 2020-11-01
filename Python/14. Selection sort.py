def sort(list):
    for i in range(len(list)):
        min = i
        for j in range(i+1, len(list)):
            if list[j] < list[min]:
                min = j
        list[i], list[min] = list[min], list[i]
        

list = [2,5,1,6,3,7,8,9,4]
sort(list)
print(list)