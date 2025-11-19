# Function bu bir marta yozib qo'yiladigan va kerak bo'lganda ishlatiladigan mini dasturcha

def salom_ber():
  print("hello world")


salom_ber()


def yigindi_1_10():
    yigindi = 0
    for son in range(1, 11):
        yigindi += son
    return yigindi

print(yigindi_1_10())

def salomlash(ism):
   print("Assalom alaykum", ism)


salomlash("Alli")


# functionda qiymat qaytarish
def toliq_ism_yasa(ism, familiya):
   toliq_ism = f"{ism} {familiya}"
   print(toliq_ism)

toliq_ism_yasa("Usmanov", "Abduqahhor")


# function return orqali biror qiymat qaytardi biz uni birin bir o'zgaruvchiga tenlab undan keyinchalik foydalanishimiz mumkin

# misloolar

def salom_ber():
   return 'Assalomu alaykum'


print(salom_ber())  # bunda hech qanday prametr berilmagan


# 2 misol

def salom_ism(ism):
   return f"Assalom alaykum {ism}!"

a = salom_ism("Abduqahhor")

print(a)

# 3 misol sonni kvadratini hisoblash

def kv_hisobla(number):
   return number **2

print(kv_hisobla(3))

# 4 misol

# 1 dan  n gacha bo'lgan sonlar yigindisini topish uchun function

def find_the_yigindi(n):
   return sum(range(1, n+1))

jami_son = find_the_yigindi(10)

print(jami_son)


# 5 misol
# juft yoki toq son ekanligin aniqlash

def aniqla(number):
   return number % 2 ==0

b = aniqla(23)
print(b)

# ********  *************

def juftmi (son):
   if son%2 ==0:
      return "Bu juft son"
   else:
      return "bu toq son"

print(juftmi(45))  # natija bu toq son, chunki 2 ga bolinganda qoldiq qoladi
