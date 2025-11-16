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

# for bilan rangni  qo'shib ishlatish
for i in range(10):
  if i % 2 == 0:
    print(i, 'just son')


# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
        print(users)

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
        print(active_users)
