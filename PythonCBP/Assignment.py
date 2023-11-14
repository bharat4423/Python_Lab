"""
 PROB-01
 """
# -------
# ['mar', 'jul', 'dec', 'sep', 'apr',  'nov', 'feb',  'may', 'oct',  'aug', 'jun', 'jan']
# sort these months using lambdas like calendar
# import time
# months = ['mar', 'jul', 'dec', 'sep', 'apr', 'nov', 'feb', 'may', 'oct', 'aug', 'jun', 'jan']
# months.sort(key=lambda m: time.strptime(m, '%b').tm_mon)
# print(months)

# Output:------
# ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
#-----------------------------------------------------------------------------------
# Prob02
# ------
# Write a code to create a identity matrix

# import numpy as np
# array_3D=np.identity(4)
# print('4x4 matrix:')
# print(array_3D)

# OutPut---
# 4x4 matrix:
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]

#-----------------------------------------------------------------------------------

# Prob03
# ------
# Write a code to create a magic matrix
# Constant = n(n**2 + 1) / 2
# 1. n / 2, n -1
# 2. r, c	=> r = r -1, c = c + 1
# 3. if r = -1	=> r = n - 1
# 4. if col = n 	=> col = 0
# 5. Position occupied -> r = r + 1, c = c - 2
# 6. r, c = (-1, n) => (0, n-2)

# import numpy as np
# def create_magic_square(N):
#     magic_square = np.zeros((N, N), dtype=int)
#     n = 1
#     i, j = 0, N // 2
#
#     while n <= N**2:
#         magic_square[i, j] = n
#         n += 1
#         newi, newj = (i - 1) % N, (j + 1) % N
#         if magic_square[newi, newj]:
#             i += 1
#         else:
#             i, j = newi, newj
#
#     return magic_square
#
# N = 3  # Replace with the desired size of the magic square
# magic_square = create_magic_square(N)
# print(magic_square)
#




