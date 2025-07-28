def arr(a):
    if len(a) < 3:
        return "Array Input Length Must More Than 2"
    else :
        a = [int(i) for i in a]
        sum = []
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                for k in range(j + 2, len(a)):
                    if a[i]+a[j]+a[k] == 0 :
                        sum.append([a[i], a[j], a[k]])
        for i in a:
            if i == 0:
                sum = [[0, 0, 0]]
    return sum

value = input("Enter Your List : ")
list = value.split()
print(arr(list))