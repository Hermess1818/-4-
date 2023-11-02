import re

print("Введите строку")
s = input()

a = re.match(r"[a-zA-Z]{2}\d{3}[a-zA-Z]",s)

if a:
    print(s)
else:
    print(s, "не номер")