# magic metods (магические методы)
# dunder methods (double underscore) -> __init__
# Служебные методы

# Магия заклбчаются в том что эти методы запускаются без прямого обращения к ним
# определенные методы могут отвечать за определенные операторы

# class A(int):
#     pass

# a = A()
# print(dir(a))

# Магические методы сравнения
# __eq__(self,other) -> 5 == 8
#                     5.__eq__(8)

# __ne__ -> !=

# __lt__ -> <

# __gt__ -> >

# __le__ -> <=

# __ge__ -> >=

# print("15"<"ABC")
# print(ord("1"),ord("a"))

# class Word(str):
#     def __new__(clc,obj):
#         # print(clc,"!!!")
#         # print(obj,"!!!")
#         obj = obj.replace(" ","")
#         return super().__new__(clc,obj)


#     def __gt__(self, other) -> bool:
#         print("gt Сработал")
#         print(self)
#         print(other)
#         return len(self) > len(other)
    
#     def __lt__(self, __value) -> bool:
#         return len(self) < len(__value)
    
#     def __eq__(self, __value: object) -> bool:
#         return len(self) == len(__value)
    

# a = Word("Hello wwwwwww")
# a1 = Word("   M a ke     rs")

# print(a > a1)
# print(a1 < a)
# print(a == a1)
#-------------------------------------------------
# + - / * // % **

# + -> __add__
# - -> __sub__
# * -> __mul__
# // -> __floordiv__
# / -> __truediv__
# % -> __mod__
# ** -> __pow__

# class Cifra:
#     def __new__(cls,*args,**kwargs):
#         num = abs(args[0])
#         instance = super().__new__(cls)
#         instance.number = num
#         return instance

#     def __add__(self,other):
#         print("add вызвана")
#         res = self.num + other.num
#         print(f"Result: {self.num} + {other.num} = {res}")

# val1 = Cifra(-117)
# val2 = Cifra(53)
# val1 + val2

###----------------------------------------------
# from random import choice


# class Dog:
#     def sound(self):
#         print("Bark!")
        
# class Cat:
#     def sound(self):
#         print("Meow Meow!")

# class Lion:
#     def sound(self):
#         print("Roar!")
        
# class Pet:
#     def __new__(cls):
#         other = choice([Dog,Cat,Lion])
#         instance = super().__new__(other)
#         print(f"I'm {type(instance).__name__}")
#         return instance
    
#     def __init__(self) -> None:
#         print("Pet never was called")

# pet = Pet()
# pet.sound()

#--------------------------
# SNGLETON

# class Singleton:
#     _instance = None

#     def __new__(cls):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance
    
#     def __str__(self) -> str:
#         return str(id(self))
    
# a = Singleton()
# b = Singleton()
# print(a)
# print(b)
# print(a is b)
#------------------------------
# дандер методы строкового отображения объктов
# __str__
# __repr__

# class Base:
#     def __init__(self,stroka) -> None:
#         self.string = stroka

#     def __str__(self) -> str:
#         return f"Object: {self.string}"
    
#     def __repr__(self) -> str:
#         return "Base('Example')"
    
# obj = Base("Jesy")
# print(obj)
# print(repr(obj))
# lal = Base("2pac")
# print(lal)
# obk2 = eval(repr(lal))
# print(obk2)

#----------------------------
# class Kopilka:
#     def __init__(self) -> None:
#         self.total = 0
#         self.coins = []

#     def add_coin(self,coin):
#         self.total += coin
#         self.coins.append(coin)

#     def __len__(self):
#         return len(self.coins)

#     def __getitem__(self,index):
#         return self.coins[index - 1]

# lol = Kopilka()
# print(lol.total)
# print(lol.coins)
# lol.add_coin(10)
# lol.add_coin(5)
# lol.add_coin(3)
# lol.add_coin(1)
# print()
# print(lol.total)
# print(lol.coins)
# print(len(lol))
# print(lol[3])

# for i in lol:
#     print(i) 