def yin_yang():
    n = int(input("Enter Input : "))
    size = 2*n + 4
    result = ""
    for i in range(0, size//2):
        for j in range(i, size//2-1):
            result += "."
        for j in range(0, i+1):
            result += "#"
        for j in range(0, size//2):
            if i == size // 2-1 or j == size // 2-1 or i == 0 or j == 0:
                result += "+"
            else:
                result += "#"
        result += "\n"
    for i in range(0, size//2):
        for j in range(0, size//2):
            if i == size // 2-1 or j == size // 2-1 or i == 0 or j == 0:
                result += "#"
            else:
                result += "+"
        for j in range(i, size//2):
            result += "+"
        for j in range(0, i):
            result += "."
        result += "\n"

    return result.rstrip()

print(yin_yang())