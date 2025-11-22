# bu o'yinda komputer son o'ylaydi biz topishga harakat qilamiz va keyin biz bir son o'ylaymiz komputer topishga harakat qiladi

import random # bu orqali biz random son olamiz


def find_number(x=10):
  tasodifiy_son = random.randint(1, x)
  print(f"Men 1 dan {x}gacha son o'yladim , Topa olasizmi?")
  taxminlar = 0
  while True:
    taxminlar += 1
    taxmin =int(input("Sonni kiriting: "))
    if taxmin<tasodifiy_son:
      print(f"Men o'ylagan son sizning taxminigizdan kattaroq , yana taxmin qilib ko'ring")
    elif taxmin>tasodifiy_son:
      print(f"Men o'ylagan son sizning taxminingizdan kichikroq")
    else:
      break
  print(f"Tabriklaymiz siz {taxminlar} taxmin bilan to'g'ri topdingiz!")
  return taxminlar

# find_number()

def find_number_pc(x=10):
  input(f"1 dan {x}gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
  quyi = 1
  yuqori = x
  taxminlar = 0
  while True :
    taxminlar += 1
    if quyi != yuqori:
      taxmin = random.randint(quyi, yuqori)
    else:
      taxmin = quyi
    javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t)"
                  f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
    if javob == "-":
      yuqori = taxmin -1
    elif javob =="+":
      quyi = taxmin+1
    else :
      break
  print(f"Men {taxminlar} ta taxmin bilan topdim!")
  return taxminlar


# find_number_pc()

def play(x=10):
  yana = True
  while yana:
    taxminlar_user = find_number(x)
    taxminlar_pc = find_number_pc(x)
    if taxminlar_user>taxminlar_pc:
      print('Men yutdim!')
    elif taxminlar_user<taxminlar_pc:
      print("Siz yutdingiz!")
    else:
      print("Durrang!")
    yana = int(input("Yana o'ynaysizmi? Ha(1)/Yo'q(0):"))

play()