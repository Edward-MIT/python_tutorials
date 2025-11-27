# Classlarda inheritance and Polimarfizm haqida

class Shaxs:
  """Shaxslar haqida ma'lumotlar """
  def __init__(self, ism, familiya, passport, tyil):
    self.ism = ism
    self.familiya = familiya
    self.passport = passport
    self.tyil = tyil

  def get_info(self):
    """Shaxs haqida malumotlar"""
    info = f"{self.ism} {self.familiya}. "
    info += f"Passport: {self.passport}, {self.ism}"
    return info
  def get_age(self, yil):
     """Shaxsning yoshini qaytaruvchi method"""
     return yil - self.tyil

inson = Shaxs("Usmanov", "Abduqahhor", 'FA435643530', 1998)

A = inson.get_info()
print(A)

#  Classdam class yaratish
# bunda biz super() metodi orqali bitta classdan ikkinchi class yaratishimiz mumkin ,haqiqiy ota classdam child classga property va methodlar hammasi voris bo'lib o'tadi

class Talaba(Shaxs):
  """Talaba Classi """
  def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
    super().__init__(ism, familiya, passport, tyil)
    self.idraqam = idraqam
    self.bosqich = 1
    self.manzil = manzil

  def get_id(self):
    """Talabaning ID raqami"""
    return self.idraqam

  def get_bosqich(self):
    """Talabaning o'qish bosqichi """
    return self.bosqich
  # Classlarda Polymarfizm tushunchasi
  # get_info methodini keling boshqatdan yozib chiqaylik
  def get_info(self):
    """Talaba haqida to'liqroq ma'lumot"""
    info = f"{self.ism}{self.familiya}. "
    info += f"{self.get_bosqich()}-bosqich Id raqam {self.get_id()}"
    return info


student = Talaba("Abduqahor", "Usmanov", "FA45325242", 1998, 2323424)

print(student.get_info())
