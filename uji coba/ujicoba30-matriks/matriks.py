'''program membuat matriks dengan ordo (2*2)'''

import numpy as np

var_A = np.array([(1,2),(-3,-1)])
print(f"Matrix a = \n{var_A}")

var_B = np.array([(2,9),(5,-4)])
print(f"Matrix b = \n{var_B}")

"""penjumlahan matriks"""

jumlah_matriks = var_A + var_B
print(f"jumlah_matriks = \n{jumlah_matriks}")

"""pengurangan matriks"""
kurang_matriks = var_A - var_B
print(f"kurang_matriks = \n{kurang_matriks}")

