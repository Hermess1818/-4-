import re
print("Введите строку")
sr = input()
if sr == '':
    print("Вы ввели пустую строку")
    exit()
else:
    sr = re.sub(r"^\s+", "", sr) # замена совпадений строки
    sr = re.sub(r"\s+$", "", sr)
    sr = sr.lower() #преобразование к нижнему регистру
    a = re.search(r"[a-z]", sr) #возвращает оъект если есть совпадение
    if a:
        sr = re.sub(r"[a-z]", a.group(0).upper(), sr, 1)
    a = re.search(r"[.!?]$", sr)
    if a:
        sr = re.sub(r"[.!?]+$", "", sr)

    sr += "."

    print("Строка преобразована: ",sr)