#  textlarni hammasi string hisoblandi
# qo'shtirnoq ichiga olingan har qanday so'z lar xattoki sonlar ham String hisoblanadi


'spam eggs'  # single quotes

"Paris rabbit got your back :)! Yay!"  # double quotes

'1975'  # digits and numerals enclosed in quotes are also strings


'doesn\'t'  # use \' to escape the single quote...

"doesn't"  # ...or use double quotes instead

'"Yes," they said.'

"\"Yes,\" they said."

'"Isn\'t," they said.'

s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), special characters are included in the string

print(s)  # with print(), special characters are interpreted, so \n produces new line


# “Agar \ bilan boshlangan belgilar maxsus belgi sifatida talqin qilinishini xohlamasangiz, satr boshidagi qo‘shtirnoqdan oldin r qo‘shib, raw (xom) stringlardan foydalanishingiz mumkin.”

print('C:\some\name')  # here \n means newline!


print(r'C:\some\name')  # note the r before the quote


# “String literal (matnli satr) bir nechta qatorga cho‘zilishi mumkin. Buni amalga oshirishning bir usuli — triple-quote ("""...""" yoki '''...''') ishlatish. Qator oxiridagi belgilar (newline) avtomatik ravishda string tarkibiga kiritiladi, lekin agar xohlasangiz, qatordan keyingi yangi qatorga o‘tishni \ qo‘yish orqali oldini olishingiz mumkin. Quyidagi misolda esa birinchi yangi qator belgisi (initial newline) string ichiga kiritilmaydi.”

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")