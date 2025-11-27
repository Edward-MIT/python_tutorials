class Avto:
  __num_avto = 0
  def __init__(self, make, model, rang, yil, narh):
    """Avtomobilning xususiyatlari """
    self.make = make
    self.model = model
    self.rang = rang
    self.yil = yil
    self.narh = narh
    Avto.__num_avto += 1
    # dunder methodlar __ (ikkita pastki chiziqcha bilan yozib hosil qilinadigan methodlardir )

  def __str__(self):
    return f"Avto: {self.make} {self.model}"

avto1 = Avto("Malibu", "Chevrolet", "Qora", 2010, 50000)
print(avto1)