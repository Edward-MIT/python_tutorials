# def  salom_ber ():

#  print("Assalom alaykum guys")

# salom_ber();

# def salom_berish_function (ism):
#    """Foydalanuvchi ismini qabul qilib olib unga salom beruvchi function!"""
#    print(f"Assalomu alaykum , hurmatli {ism.title()}")



# salom_berish_function("hasan ")


#  NESTING

car_0 = {
  'model': 'Tesla',
  'rang': "oq",
  'yil': 2022,
  'narx': 20000,
  'km': 62000,
  'karobka': "avtomat"
}

car_1 = {
  'model': 'BMW',
  'rang': "oq",
  'yil': 2021,
  'narx': 20000,
  'km': 340000,
  'karobka': "avtomat"
}

car_2 = {
  'model': 'Mersedes-Benz',
  'rang': "kok",
  'yil': 2022,
  'narx': 20000,
  'km': 120000,
  'karobka': "avtomat"
}

# car = car_0
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang "
#       f"{car['yil']} -yil, {car['narx']}$")

# cars = [car_0, car_1, car_2]

# for car in cars :
#   print(f'{car["model"].title()}, '
#         f'{car["rang"]} rangda,  '
#          f'{car["yil"]}- yilda ishlab chiqarilgan, '
#          f'{car["narx"]}$ ga sotamiz')


# print(cars[0]);

# print(cars[0]["model"])

malibus = []

for m in range (5):
  yangi_mashina = {
    'model': 'malibu',
    'rang': None,
    'yil': 2025,
    'narx': None,
    'km': 0,
    'karobka': 'auto',
  }

  malibus.append(yangi_mashina)

#   print(malibus)

  for impala in malibus:
    print(impala)