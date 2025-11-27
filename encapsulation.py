# Classlarda encapsulation - bu objectlarni biron bir hususiyatini yashirishga aytiladi

from uuid import uuid4;

class Avto:
  """Avtobilllar haqida class"""
  def __init__(self, make, model, rang, yil, narh, km = 0 ):
    """ Avtomibilening hususiyatlari"""
    self.make = make
    self.model = model
    self.rang = rang
    self.yil = yil
    self.narh = narh
    self.__km = km  # private qilib qo'ydik
    self.__id = uuid4()  #private qilib qo'ydik

  def get_km(self):
    return self.__km

  def get_id(self):
    return self.__id

  def add_km(self, km):
    """Mashinanig yurganiga yana km qo'shilishis mumkin"""
    if km>=0:
      self.__km += km
    else:
      print("Mashinanig km ni kamaytirib bo'lmaydi")

avto1 = Avto("GM", "Malibu", "qora", 2020, 20000, 10000)

avto1.add_km(30000)

print(avto1.get_km())
