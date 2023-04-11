x=input("Введите перове число: ")
if x.isdigit():
      i=int(x)
else:
    raise ValueError("Неверный ввод первого числа")

y=input("Введите второе число: ")
if y.isdigit():
    j=int(y)
else:
    raise ValueError("Неверный ввод второго числа")

z=input("""Выберите действие из перечисленных:\n+ - сложение\n- - вычитание\n* - умножение
/ - деление\n% - остаток от деления\n** - возведение в степень\n// - деление без остатка\n""")
        
if z=="+":
    print(f"Ответ:{i+j}")
elif z=="-":
    print(f"Ответ:{i-j}")
elif z=="*":
    print(f"Ответ:{i*j}")
elif z=="/":
    print(f"Ответ:{i/j}")
elif z=="%":
    print(f"Ответ:{i%j}")
elif z=="**":
    print(f"Ответ:{i**j}")
elif z=="//":
    print(f"Ответ:{i//j}")
else:
    print("Данной операции нет в системе")