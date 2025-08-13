def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def last(purity):
    if purity == 1:
        return 1
    return ((last(purity - 1) * 2) + fibo(purity - 1)) // 2 

def forge(weight, purity):
    purity = purity - 1
    if purity == 0:
        return weight
    ck = fibo(purity)
    weight = (2 * weight) + 1 - ck
    if weight <= 1:
        return -1
    
    def weight_distribute(weight):
        a = last(purity)
        b = weight - a
        if a > b:
            return -1
        w1 = forge(a, purity)
        w2 = forge(b, purity)
        if w1 == - 1 or w2 == -1:
            return -1
        return w1 + w2

    return weight_distribute(weight)

purity, weight = input("Purity and Weight needed: ").split()
purity, weight = int(purity), int(weight)
if purity == 1:
    print(f"Total weight of used minerals with Purity 1 : {weight}")
else:
    print(f"Total weight of used minerals with Purity 1 : {forge(weight, purity)}")