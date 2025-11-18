# for yoki while sikllarida break operatori else qismi bilan birga ishlatilishi mumkin. Agar sikl break bajarilmasdan tugasa, else qismi bajariladi.

# for siklida, agar break ishlamagan bo‘lsa, sikl oxirgi iteratsiyasini tugatgandan keyin else qismi bajariladi.

# while siklida, shart yolg‘onga aylangandan keyin va break ishlamagan bo‘lsa, else bajariladi.

# Har ikkala siklda ham, agar sikl break orqali to‘xtatilgan bo‘lsa, else qismi bajarilmaydi. Albatta, siklni oldinroq tugatadigan boshqa holatlar ham bor — masalan, return ishlatilsa yoki xatolik (exception) yuzaga kelsa — bular ham else bajarilishini to‘xtatadi.

for i in range(5):
    print(i)
    if i == 2:
        break
else:
    print("Bu matn chiqmaydi!")  # natija 0, 1, 2  i == 2 bo'lganda break ishladi -> else bajarilmadi


for n in range (2, 10):
    for x in range(2 , n):
        if n%x == 0:
            print(n, 'equals', x, "*", n//x)
            break
        else:
            print(n, 'is a prime number!')
