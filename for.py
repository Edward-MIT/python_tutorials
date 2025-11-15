# 1.list bo'yicha for

fruits = ['apple', 'banana', 'cherry']

for a in fruits:
  print(a)

  # python har bir elementni f o'zgaruvchisiga beradi

# 2. String bo'yicha for

for a in 'hello':
  print(a)

# 3. range() bilan for

for i in range(5):
  print(i)

# range (start, stop, step)

for x in range(3, 15, 5):
  print(x)

# for bilan i qo'shib ishlatish
for i in range(10):
  if i % 2 == 0:
    print(i, 'just son')