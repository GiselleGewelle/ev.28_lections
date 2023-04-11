# string - строки 
"hello world true 5 None"
"""Hello world
My name is Anton
"""
# Строки - набор последовательных символов которые мы используем для хранения и представления текстовой инфы
# Индексация в сторке
#name = "john"
#j
#o
#h
#n
# print(name)
# print(name[0],name[1],name[2],name[3])

# # index [-1] - последний символ

# str1="kani"
# print(str1[-1],str1[0])

# str1="birthday"
# print(str1[5]+str1[6]+str1[7])
# print(str1[0]+str1[1]+str1[2]+str1[3]+str1[4])

# срезы по индексам
# # [start:emd:<step>]
# x="birthday"
# print(x[5:],x[:5])

# text="Hello world! My name is JOHN I'm King of North "
# # print(text[:13],text[:  :2])
# print(text[::-1])

# Конкатенация строк(соединение)
# a="hello"
# b="world"
# c=" "
# print(a+c+b)

# экранирование - способ записи символов в строку, которые невозможно ввести с клавиатуры
# \n -> перенос строки
#\t -> горизонтальная табуляция(отступ)
#\v -> вертикальная табуляций
#\f -> перевод страницы
#\r -> возврат указателя
# print("\vhello \tworld!\nMy name is john snow")

# форматирования строк
# 1.с помощю знака %
# 2.с исользованием /format()
# 3.Инtерполяция строк

# %
# name=input("vvedite imya:")
# lastName=input("vedite familiyu:")
# # print("dobro pojalovat k nam " + name + " " + lastName+ "!")
# print("Hello mr/mrs %s %s!" %(name,lastName))

# .format
# name=input("vvedite imya:")
# lastName=input("vedite familiyu:")
# print("Privetstvuy vas,{} {}, v nas club".format(name,lastName))

# Интерполяция строк - преобразование,f-stroki
# f-stroki
# a=input("Enter mr/mrs:")
# name=input("vvedite imya:")
# lastName=input("vedite familiyu:")
# print(f"hello {a} {name} {lastName}! Welcome to the parthy")

# # len - выводит количество символов в строке
# text="Запомни Питтер, с большоай силой приходит и большая ответственность."
# reversed_text=text[::-1]
# print(reversed_text)
# i=0
# lol_t=0
# lenText=len(reversed_text)
# while i<lenText:
#         symbol=reversed_text[i]
#         if symbol == "т" or symbol == "Т":
#             lol_t+=1
# # print(symbol)
#         i+=1
# print(f"V texte't' vstretilas {lol_t} raz")
        
        