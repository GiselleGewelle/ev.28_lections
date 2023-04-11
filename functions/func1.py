# найти квадрат,куб,ркзультат деления на 100
# num1=5
# ->{"2":25,"3":125,"100":0.05}
# num1=5
# num2=16
# num3=28
# num4=1154
# num5=31

# # print({"2":num1**2,"3":num1**3,"100":num1/100})
# # print({"2":num2**2,"3":num2**3,"100":num2/100})
# # print({"2":num3**2,"3":num3**3,"100":num3/100})
# # print({"2":num4**2,"3":num4**3,"100":num4/100})
# # print({"2":num5**2,"3":num5**3,"100":num5/100})

# def operations(num):
#     print({"num":num,"2":num**2,"3":num**3,"100":num/100})
# operations(num1)
# operations(num2)
# operations(num3)
# operations(num4)
# operations(num5)

#-------------------------------------------------------------------------------

# функция это именованая часть программы которая содержит в себе определенный набор иинструкций
# и может вызываться в других частях программы сколько угодно при помощи названия

# def name_of_function(<a,b> параметры):
#     <body> -> код, какая то логика которая будет давать конечный результат
#     <return> -> оператор который помогает вернуть результатu


# name_of_function(5,7 -> аргументы)

# Параметры функции - переменные которые будут принимать данные от пользователя и хранить в себе эти данные

# аргументы функции - данные которые мы передаем функции в моменте вызова

# print(len("lol"))
# ls=[1,2,3,4,5]
# str1="Hello world! S vami Sans adn Pops!"

# def our_len(a):
#     i=0
#     print(a)
#     for x in a:
#         i+=1
#     print(f"result: {i}")

# print(our_len(ls))
# print(our_len(str1))

# def isEven(obj):
#     # if obj%2==0:
#     #     return True
#     # else:
#     #     return False
#     return True if obj%2==0 else False
# print(isEven(5))

# words=["John","Ono","kazak","peter","Dovod","radar","apa","lol"]
# def get_polindrom(words):
#     newlist=[]
#     for i in words:
#         if i.lower() == i[::-1].lower():
#             newlist.append(i)
#     return newlist
        
# print(get_polindrom(words))


# def depozit(money,period):
#     if money < 30000:
#         raise ValueError("Вложить можно толбко болше 30000")
#     elif period < 3:
#         raise ValueError("Период должен быть больше 3 лет")
#     year=0
#     while year<period:
#         money+=money*0.1
#         year+=1
#     return money
# money=float(input("Enter the sum: "))
# period=int(input("Enter period: "))
# print(depozit(money,period))

# def isEven(x: int) -> bool:
#     """
#     Our function returns True or False while checking number for even number 
#     """
#     # Запись подсказки к использованию функции
#     return True if x%2==0 else False
# print(isEven(5))

# try:
#     n=int(input("Vvide chislo: "))
# except ValueError:
#     print("Wrong number!")
# else:
#     dict_={x:x**2 for x in range(1,501) if x%n==0}

# print(dict_)
