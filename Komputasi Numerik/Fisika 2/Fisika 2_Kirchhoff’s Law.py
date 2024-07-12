def gauss_jordan(a, b):
    n = len(b)

    # Augmented matrix
    for i in range(n):
        a[i].append(b[i])

    # Forward elimination
    for i in range(n):
        # Search for maximum in this column
        max_el = abs(a[i][i])
        max_row = i
        for k in range(i+1, n):
            if abs(a[k][i]) > max_el:
                max_el = abs(a[k][i])
                max_row = k

        # Swap maximum row with current row (column by column)
        for k in range(i, n+1):
            a[max_row][k], a[i][k] = a[i][k], a[max_row][k]

        # Make all rows below this one 0 in current column
        for k in range(i+1, n):
            c = -a[k][i] / a[i][i]
            for j in range(i, n+1):
                if i == j:
                    a[k][j] = 0
                else:
                    a[k][j] += c * a[i][j]

    # Solve equation for an upper triangular matrix
    x = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = a[i][n] / a[i][i]
        for k in range(i-1, -1, -1):
            a[k][n] -= a[k][i] * x[i]
    return x

# Matriks koefisien
A = [
    [6, 4, 0],
    [0, 4, 8],
    [6, 0, -8]
]

# Matriks hasil
B = [12, 9, 0]

# Memanggil fungsi gauss_jordan untuk menyelesaikan persamaan
result = gauss_jordan(A, B)

# Menampilkan hasil
I1, I2, I3 = result
print(f"Arus melalui R1 (I1) = {I1:.2f} A")
print(f"Arus melalui R2 (I2) = {I2:.2f} A")
print(f"Arus melalui R3 (I3) = {I3:.2f} A")
