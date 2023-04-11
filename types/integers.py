# типы данных числа -> int,float
# = -> оператор присваивания 
# variable(переменая)
# num=5
# print(num)
# num=79 # переопределение
# print(num)

# # abc-> Нижний регистр
# # ABC -> Верхний регистр 
# # PEP8

# num1 = 5
# num2 = 15
# result = num1 + num2
# print('summa',result)

# num1 = input("Enter the num1: ")
# num2 = input("Enter the num2: ")
# num1 = int(num1)
# num2 = int(num2)
# print(num2 - num1)
# num1 = int(input("Enter the num1: "))
# num2 = int(input("Enter the num2: "))
# print(num1,"*",num2,"=",num1*num2)
# / - // - %
# / - обычное деление
# // - деление без остатка 
# % - модульное(получение остатка от деления)

# num1 = 7
# num2 = 3
# print("/",num1/num2)
# print("//: ",num1//num2)
# print("%: ",num1%num2)

# ** - Возведение в степень
# print(5 ** 5)
# ** 0.5 - квадратный корень числа
# print(9 ** 0.5)
 
# pow - возведение в степень
# pow(num1, num2, <mod>)

# num1 = 5
# num2 = 10
# print (pow(5,10, 65))
# a = 5
# b = 2
# res = pow(a,b,12)
# print(res)

# round() - округление числа с плавающей точкой

# a=5.61421
# print(round(a,2))

# abs()- абсолютное значение числа
# a = abs(-16)
# b=abs(23)
# print(a,b)

# divmod(a,b) - выводит два числа, первое число это результат целочисленного деления а на б , а второе это модульное деление 

# res = divmod(5,2)
# print(res)

# import math
# a=5
# print(round(math.sqrt(a),2))

# множественное присваисвание 
# оператор присваивания - (=) 
# a=5
# b=15
# c= None

# # c = a
# # a = b
# # b = c 
# a, b = b, a
# print("a:",a,"b:",b)
# num1,num2,num3=input("num1:"),input("num2:"),input("num3:")
# print(num1)
# print(num2)
# print(num3)
# from math import pi
# r=int(input("Введите радиус:")) 
# res_P=2 * r * pi
# res_S= pi *(r**2)
# print("Ploshad:",round(res_S,2),"Perimetr:",round(res_P,2))
# import math - импортирует все библиотеку
# from math import pi, sqrt - импортирует определенные каманды из библиотеки

# from random import randint

# # print(randint(1,10))
# name=input("vvedite imya:")
# lastName=input("vveditr familiy:")
# num=randint(1000000,9999999)
# print(name,lastName,num)
# res=name+lastName+str(num)
# print(res)

# from random import randint

# num=randint(1,10)

# i=0
# while i<3:
#     guess=int(input("ugadai chislo:"))
#     if guess ==num:
#         print("pobeda:")
#         break
#     i=i+1
#     i+=1 инкремент
