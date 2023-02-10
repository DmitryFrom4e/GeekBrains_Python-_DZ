# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# 1. возможно что то неправильно... есть сомнения 
import math
pi1 = 1
n = int(input('введите точность для pi: '))
for i in range(n):
    pi1 = math.sqrt(2 + pi1)
pi1 = 3 * (2 ** n) * math.sqrt(2 - pi1)
print(round(pi1, n))

# 2. другой способ, нагуглил - тоже сомневаюсь
from math import pi

print(round(pi, n))
