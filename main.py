# lambda function

import math
uzunlik = lambda pi, r: 2*pi*r
print (uzunlik(math.pi,10))


# ikkinchi misol

kvadrat = lambda x, y : x**y
print(kvadrat(3, 2))


# uchinchi misol

def daraja (n):
  return lambda x : x**n
kvadrat=daraja(5)

print(kvadrat(5))