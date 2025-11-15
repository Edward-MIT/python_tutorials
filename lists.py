# “Python bir nechta murakkab (compound) ma’lumot turlarini biladi, ular boshqa qiymatlarni bir joyga jamlash uchun ishlatiladi. Eng qulayi — bu ro‘yxat (list). Ro‘yxat kvadrat qavslar ichida vergul bilan ajratilgan elementlar ko‘rinishida yoziladi. Ro‘yxatlar turli xil turdagi elementlarni ham o‘z ichiga olishi mumkin, lekin odatda ularning barchasi bir xil turdagi bo‘ladi.”

squares = [1, 4, 9, 16, 25]
print(squares)

a = squares[0] # listdagi o chi ingeksdagi raqamni a ga tengladik   a = 1
print(a)

b = squares[-1]# -1 chi indeks bu listdagi eng oxirgi belgini chiqarib beradi
print(b)

c = squares[-3:] #natija oxirgi belgidan orqaga 3 ta belgini chiqarib beradi
print(c)


# listlar ustida amamllarini bajarsa ham bo'ladi
x = squares +[36, 49, 64]
print(x)

# Stringlardan farqli o‘laroq, ular o‘zgarmas (immutable) bo‘lsa, listlar o‘zgaruvchan (mutable) turga kiradi. Ya’ni, ro‘yxatning ichidagi elementlarni keyinchalik o‘zgartirish mumkin.

cubes = [1, 8, 27, 65, 125]  # something's wrong here
4 ** 3  # the cube of 4 is 64, not 65!

cubes[3] = 64  # replace the wrong value
print(cubes)

# listlarga turli hil methodlardan foydalanib listlarga o'zgartirishlar kiritishimiz mumkin

# list.append()  append methodi listga qo'shimcha element qo'shadi

cubes.append(216)
cubes.append(7**3)
print(cubes)

# Python’da oddiy o‘zgaruvchini qiymatga tenglashtirish (assignment) hech qachon ma’lumotni nusxalamaydi. Agar siz ro‘yxatni (listni) biror o‘zgaruvchiga bog‘lasangiz, o‘sha o‘zgaruvchi asl ro‘yxatga ishora qiladi. Ro‘yxatni bitta o‘zgaruvchi orqali o‘zgartirsangiz, o‘sha ro‘yxatga ishora qilayotgan boshqa barcha o‘zgaruvchilar ham bu o‘zgarishni ko‘radi.

# bu nimani anglatadi oddiy qilib tushuntirish

a = [1, 2, 3]
b = a
a[0] =100  # bu yerda a ning o chi indeksidagi 1 ,1oo ga o'zgardi

# bu yerda python ro'yhatni nusxalamaydi , shunchaki ikkinchi nom beradi, a ni o'zgartirganingiz b ga ham tasir qiladi, b ni o'zgartirganingiz a ga ham tasir qiladi

print(b)  #natija [100, 2, 3]



rgb = ['Red', 'Green', 'Blue']

rgba = rgb
id(rgb) == id(rgba) #they reference the same object

rgba.append("Alpha")

print(rgb)


# list.len() methodi listni ichida nechta element borligini aniqlanb beradi

letters = ['a', 'b', 'c', 'd']
len = len(letters)
print(len)


# ro'yhat ichida yana ro'yhat hosil qilib uni nested qilish mumkin

h = ['a', 'b', 'c', 'd']
w = [1, 3, 5]

d = h+w
print(d)

print(d[0])
