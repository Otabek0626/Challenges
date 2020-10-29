def count_substring(string, sub_string):
    string = list(string)
    sub_string = list(sub_string)
    ans = []
    for i in range(len(string)):
        data = []
        for j in range(len(sub_string)):
            if i+j < len(string):
                data.append(string[i+j])
        ans.append(data)
        a = 0
        for i in ans:
            if i == sub_string:
                a+=1
    return a

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
