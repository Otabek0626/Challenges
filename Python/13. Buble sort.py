def sort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
        
        

list = [2,5,1,6,3,7,8,9,4]
sort(list)
print(list)