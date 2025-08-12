import math
"""
print(format(math.pi, '.12g'))
print(format(math.pi, '.2f'))
print(repr(math.pi))

print(0.1 + 0.1 + 0.1 == 0.3)
print(round(0.1, 1) + round(0.1, 1) + round(0.1, 1) == round(0.3, 1))
print(math.isclose(0.1 + 0.1 + 0.1, 0.3))
print(round(math.pi, ndigits=2) == round(22 / 7, ndigits=2))

"""

"""
x = 3.14159
print(x.as_integer_ratio())

print(x == 3537115888337719 / 1125899906842624)
print(x.hex())

print(x == float.fromhex('0x1.921f9f01b866ep+1'))


arr = [-0.10430216751806065, -266310978.67179024, 143401161448607.16,
       -143401161400469.7, 266262841.31058735, -0.003244936839808227]

print(math.fsum(arr))

print(sum(arr))
total = 0.0
for x in arr:
    total += x
print(total)
"""

# 15.1 Representatin Error

"""
print(2**52 <= 2**56 // 10 < 2**53)

q, r = divmod(2**56, 10)
print(r)

print(q+1)

print(format(0.1, '.17f'))
"""

"""
from decimal import Decimal
from fractions import Fraction

print(Fraction.from_float(0.1))
print((0.1).as_integer_ratio())
print(Decimal.from_float(0.1))
print(format(Decimal.from_float(0.1), '.17'))
"""