

# pythond xatolar bilan ishlash, xatolarni catch qilish uchun biz try except operatorodan foydalanamiz



age = input("Enter your age: ")
try:
    age = int(age)
    print (f'You are born {2025 - age} year')
except:
    print("you have to input deciminla number")



print ("your programm is running ")