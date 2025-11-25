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
     return yil - self.tyil