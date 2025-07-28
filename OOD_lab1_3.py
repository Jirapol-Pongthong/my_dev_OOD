def pascal_triangle(n):
    triangle = []

    for row_num in range(n):
        row = [1]  # ตัวแรกเสมอเป็น 1
        if triangle:
            last_row = triangle[-1]
            for i in range(1, row_num):
                row.append(last_row[i - 1] + last_row[i])
            row.append(1)  
        triangle.append(row)

    return triangle


n = int(input("Enter number of row : "))
triangle = pascal_triangle(n)
for row in triangle:
    print(' '.join(str(num) for num in row))