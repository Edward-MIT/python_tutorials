# Agar siz sonlar ketma-ketligi ustida aylantirib chiqishingiz (iteratsiya qilishingiz) kerak bo‘lsa, range() degan ichki funksiyadan foydalanish juda qulay. U arifmetik progressiyalarni yaratadi.

for i in range(19):
  print(i)


# Berilgan oxirgi nuqta (end point) hech qachon yaratilgan ketma-ketlikka kirmaydi; masalan, range(10) 10 ta qiymat hosil qiladi — bu 10 uzunlikdagi ketma-ketlik uchun to‘g‘ri indekslar. range boshqasidan boshlash, yoki boshqa qadam (step) bilan ishlash imkonini ham beradi. Qadam salbiy ham bo‘lishi mumkin

print(list(range(5,10)))

# range (start, stop, step)

print(list(range(0, 10, 3)))

print(list(range(-100, -10, 30)))

# To iterete over the indices of a sequence, you can combine range() and lem() as follows:
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])