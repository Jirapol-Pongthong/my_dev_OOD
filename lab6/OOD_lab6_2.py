def sum_digit(num):
    if num < 10:
        return num
    sum = num%10
    return sum + sum_digit(num//10)

def lucky_number(num,sum_time = 1):
    sum = sum_digit(num)
    if sum // 10 == 0:
        return  print(f"Lucky Number: {sum_digit(num)}")
    else:
        print(f"Sum #{sum_time} : {sum_digit(num)}")
        
        return lucky_number(sum_digit(num),sum_time+1)

inp = input("Enter Input: ")
lucky_number(int(inp))



