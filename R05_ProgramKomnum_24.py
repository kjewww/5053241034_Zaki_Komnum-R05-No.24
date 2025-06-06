import numpy as np
import pandas as pd

# Data
x = np.array([6, 9, 12, 15], dtype=float)
y = np.array([234, 960, 2280, 4356], dtype=float)

# Tabel beda terbagi
n = len(x)
div_diff = np.zeros((n, n))
div_diff[:, 0] = y

for j in range(1, n):
    for i in range(n - j):
        div_diff[i][j] = (div_diff[i + 1][j - 1] - div_diff[i][j - 1]) / (x[i + j] - x[i])

# Fungsi interpolasi Newton
def newton_interpolation(x_eval):
    result = div_diff[0][0]
    product_term = 1.0
    for j in range(1, n):
        product_term *= (x_eval - x[j - 1])
        result += div_diff[0][j] * product_term
    return result

# Tampilkan tabel
df = pd.DataFrame(div_diff, columns=[f"Derajat {i}" for i in range(n)])
df.insert(0, "x", x)
print("\nTabel Beda Terbagi (ordo 0-3)")
print(df.to_string(index=False))

# Evaluasi f(11)
f11 = newton_interpolation(11)
print("\nHasil Interpolasi Newton")
print(f"f(11) = {round(f11, 2)}\n")