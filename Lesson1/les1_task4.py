# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
a = (input("Введите первую букву")).lower()
b = (input("Введите вторую букву")).lower()
a = ord(a) - 96
b = ord(b) - 96
if a==b:
    print(f'Порядковый номер первой буквы {a}, второй - {b}')
    print(f"Между первой и второй буквой 0 букв")
else:
    print(f'Порядковый номер первой буквы {a}, второй - {b}')
    print(f"Между первой и второй буквой {abs(b - a) - 1} букв")
