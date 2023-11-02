import re
while True:
    print("Введите строку")
    a = input()
    if a == '':
        print("Пустая строка")
        exit()
    else:
        if re.match(r"[^\\<>/|?*\"]+\.(txt|doc|docx|odt|rtf)", a):
            print(a, "- является файлом")
