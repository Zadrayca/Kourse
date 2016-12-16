
from decimal import Decimal
# print(0.1 + 0.1 + 0.1 == 0.3)
#
# d = Decimal('0.1')
# print(d)
#
# print(d + d + d == Decimal('0.3'))

result = (Decimal('0.5') + Decimal('0.5') ** Decimal('2') / Decimal('2'))
print(float(result))

from decimal import getcontext

print(getcontext().prec)

getcontext().prec = 10
print(Decimal('0.88474'))

x = (Decimal('0.3') / Decimal('150'))
print(x)