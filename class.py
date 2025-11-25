# classlar bir biriga o'xshash bo'lgan objectlarni yaratishda bizga yordam beruvchi shablon hisoblanadi. biz bir class yaratib olganimizdan keyin undan neshta object yaratishimiz mumkin va ular ham bir xil xususiyatlarga ega bo'ladi.

class Talaba():
  def __init__(self, name, surname, birthday):
    self.name = name
    self.surname = surname
    self.birthday = birthday

  def get_name(self):
    return self.name

  def get_age(self, yil):
    return yil- self.birthday

  def introduce (self):
    print(f"Ismim{self.name} tug'ulgan yilim {self.birthday}")

# bu classdan foydalanib biz objectlar yaratishimiz mumkin

talaba1 = Talaba("Ali", "Valiyev", 1998)

a = talaba1.name
b = talaba1.introduce()
c = talaba1.get_age(2025)

print(a)
print(b)
print(c)


# ikkinchi class

class Fan():
  """Fan nomli class"""
  def __init__(self, nomi):
    self.nomi = nomi
    self.talabalar_soni = 0
    self.talabalar = []

  def add_student(self, talaba):
    """Fanga talabalar qo'shish"""
    self.talabalar.append(talaba)
    self.talabalar_soni += 1

  def get_fullname(self):
    return self.nomi

  def get_students (self):
    """Fanga yozilgan talabalar haqida ma'lumot"""
    return [talaba.get_fullname() for talaba in self.talabalar]



matem = Fan("Matematika")
print (matem.talabalar)

print(talaba1.name)

matem.add_student(talaba1)
c = matem.talabalar_soni
print(c)

talaba2 = Talaba("Usmanov", "Abduqahhor",1998)
matem.add_student(talaba2)

d = matem.talabalar_soni
print(d)
