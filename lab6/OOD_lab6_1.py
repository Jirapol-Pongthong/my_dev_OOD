def min (number,n = 0,cur_min = None):
    if n >= len(number):
        return cur_min
    num = int(number[n])
    if cur_min is None or cur_min > num:
        cur_min = num
    return min(number,n + 1,cur_min)

           

inp = input("Enter Input : ")
inp = inp.split()
value=min(inp)
print(f"Min : {value}")

