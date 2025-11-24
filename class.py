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
