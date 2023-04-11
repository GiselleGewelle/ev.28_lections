# print(dir(str))
# print(dir(int))

# a="hello"
# b="john"
# # print(a!=b)
# # print("abc"=="abc")
# print(a>b)
# print(a<b)
# print("a") #97 -> 110001
# print("a">"b")

# print("hello">"harry")
# print("abc">"abc")

# len- возвращает количесвто символов в строке
# a='hello'
# b="john snow"
# print(len(a)<len(b))
# print(len(a),len(b))

# методы строк
# replace(old,new,[count])- меняет в строке символы old на new, если вы укажете count, то заменит count раз
# replace - можно применять только на строки
# text="ha ha ha ha"
# result=text.replace("a","e",3)
# print(text)
# print(f'result after replace:{result}')

# str1="hello world! My name is John Snow!"
# result=str1.replace("John Snow","Alan Walker")
# print(result)

# strip() - убирает пробельные символы в начале и в конце строки
# rstrip, lstrip
# a="   hello   "
# print(len(a))
# print(a)
# res=a.lstrip()
# print(len(res))
# print(res)

# print(dir(str))

# isdigit-     проверяют
# isnumeric -  состоит ли наша строка
# isdecimal -  полностью из чисел

# num=input("vvedite chislo:")
# print(f"Vvedeno chislo?: {num.isdigit()}")

# num=input("vvedite chislo:")
# if num.isdigit():
#       num=int(num)
#       print(f"{num} + 5 = {num+5}")
# else:
#       print("vi vveli ne chslo")

# text="\u0031"
# print(text)
# print(text.isnumeric())
# print(text.isdecimal())

# isalnum - проверякт состоит ли наша строка из чисел и символов латинского алфавита и киррилицы
# str1="載于玉函山房輯佚"
# print(str1.isalnum())
# str2="56_a"
# print(str2.isalnum())

# isalpha() -> состоит ли наша строка полностью из символов алфавита

# text="Hello world"
# res=text.replace(" ","")
# print(text.isalpha())
# print(res.isalpha())

# islower()
# isupper()
# istitle()

# str1="Is"
# print(str1.islower()) - все символы в нижнем регистре

# str2="IS"
# print(str2.isupper()) - все символы в верхнем регистре

# str3="Is"
# print(str3.istitle()) - первый символ каждого слова в верхнем регистре


# index(value,[star],[end]) - выводит индекс значения value которые мы передаем в нашей строке

# text='Hello'
# print(text.index("l",3))
# text="Hello world! My name is John Snow!"
# res=text.index("o")
# print(res)
# res=text.index("o",res+1)
# print(res)
# res=text.index("o",res+1)
# print(res)
# res=text.index("o",res+1)
# print(res)

# count(value,[start]) - считает кол-во вхождений value в нашу строку
# text="hello o o o hello"
# print(text.count("hello"))

# split(separator) - дробит нашу строку на несколько частей по разделителю. все части строк сохраняются в типе list
# text="You want to play, Lets play"
# res=text.split(" ")
# print(res)
# print(len(res))
# a="Hello#Hello#Hello#Hello"
# res=a.split("#")
# print(res)

# "connector".join(list) - соединяет по connector строки которые находились в list

# text="You want to play, Lets play"
# res=text.split(" ")
# print(res)
# str1=" ".join(res)
# print(str1)

# find(value, [start],[end]) - делает то же саме что и индекс, но если не нашел то вренет -1

# text='hello'
# print(text.find('l'))
# print(text.find('lytui'),type(text.find('lytui')))

#swapcase() - переводит все символы в противоположный рнгистр
#uper()- переводит все символы в верхний регистр
# lower()- переводит все символы в нижний регистр

# text="Hello WOrLd! My NAme is JOHN snow"
# print(text.upper())
# print(text.lower())
# print(text.swapcase())
# print(f"Original {text}")

# capitalize() - переводит самый первый символ в верхний регистр
# title() - переводит все первый символы всех слов в верхний регистр
    
# name=input("vvedite imya:").capitalize()
# print(name)
# print(f"Hello mr/mrs {name}")

# fio="gol.d.rodger"
# print(fio.title())
