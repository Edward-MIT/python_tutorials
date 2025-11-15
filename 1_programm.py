# Fibonacci series :
# the sum of two elements defines the next

a, b = 0, 1

while a < 10:
  print (a)
  a, b = b, b+a


# if statement in python


x = 20

if x >10:
  print("x 10 dan yuqori")

# if else
c = 3
if c>5:
  print("c 5dan yuqori")
else:
  print("c biz o'ylagan son")

# if elif -else

x = 10

if x > 15:
  print("15 dan katta son")
elif x==20:
  print("siz o'ylagan son  aynan 20")
else:
  print('men buni bilmayman')


# keyingi mashq

x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')