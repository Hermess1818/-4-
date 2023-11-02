import re

print("Введите первую строку")
sn1 = input()

print("Введите вторую строку")
sn2 = input()

a = re.findall(sn2,sn1)

if not a:
    print("Нет вхождений второй строки в первую")
    exit()
else:
    otv = re.sub(sn2,"",sn1,len(a)-1)
    print(otv)