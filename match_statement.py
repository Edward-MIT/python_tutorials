# match operatori (Python 3.10 dan boshlab) biror ifodani oladi va uning qiymatini ketma-ket berilgan pattern (andazalar) bilan solishtiradi. Har bir pattern alohida case blokida yoziladi.

# Bu C, Java yoki JavaScript dagi switch operatoriga o‘xshab ketadi, lekin uning mantig‘i Rust yoki Haskell dagi pattern matching ga ancha yaqinroq.

# Qaysi pattern birinchi bo‘lib mos kelsa — faqat o‘sha case bajariladi.

# Agar kerak bo‘lsa, match operatori qiymatdan ayrim qismlarni (masalan, list elementlari yoki obyekt attributlari) ajratib olib o‘zgaruvchilarga yuklab ham bera oladi.

# Agar hech bir case mos kelmasa — hech qanday bo‘lim bajarilmaydi.

def check_value(val):
    match val:
        case 1:
            print("Bu 1")
        case 2:
            print("Bu 2")
        case [a, b]:
            print("Bu ikki elementli ro'yxat:", a, b)
        case _:
            print("Hech bir case mos kelmadi")

check_value([10, 20])


def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
