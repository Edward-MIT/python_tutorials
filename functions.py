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