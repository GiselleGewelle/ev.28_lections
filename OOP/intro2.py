# class Human:
#     age=0

#     def __init__(self,name,last_name,weight,nation):
#         self.name=f"{name} {last_name}"
#         self.weight=weight
#         self.nationality=nation

#     def birthday(self):
#         from random import randint
#         print(f"\nHappy Birthday, {self.name}!!!")
#         self.age+=1
#         self.weight+=randint(3,7)

#     def show_info(self):
#         print(f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}, Nation: {self.nationality}")
        
# human1 = Human("John","Snow",3.3,"American")
# human2 = Human("Abu-Bakr","Al-Nasar",3.8,"Arabic")

# human1.show_info()
# human2.show_info()

# human1.birthday()
# human2.birthday()

# human1.show_info()
# human2.show_info()
#-----------------------------------------------------------
# class Student:
#     univer="Harvard University"

#     def __init__(self,name):
#         self.name = name
#         self.books = []
#         self.languages = {}
#         self.knowledge = 0
#         self.ready_to_work = False
    
#     def add_points(self,points):
#         self.knowledge += points
#         if self.knowledge > 500 and not self.ready_to_work:
#             self.ready_to_work = True
#             print(f"{self.name} get 500 points")
        
#     def read_book(self,book_name):
#         self.books.append(book_name)
#         self.add_points(50)

#     def do_project(self):
#         self.add_points(100)

#     def lern_new_language(self,language,percent):
#         if percent not in range(70,100):
#             print("Invalid Points")
#         else:
#             self.languages[language] = percent
#             self.add_points(percent)

# st1 = Student("John Snow")
# st2 = Student("Aizirek Akimbaeva")

# print(st1.name)
# print(st2.name)

# print(f"Before study {st1.name}: {st1.books}, {st1.languages}, {st1.knowledge}")
# print(f"Ready to work: {st1.ready_to_work}")

# st1.read_book("Song of ice and fire")
# st1.read_book("Algaritms and Data Structures")
# st1.read_book("Eugene Onegin")
# st1.read_book("Martin Eden")

# st1.do_project()
# st1.do_project()

# st1.lern_new_language("Python",40)
# st1.lern_new_language("Python",90)
# st1.lern_new_language("C++",75)

# print(f"After study {st1.name}: {st1.books}, {st1.languages}, {st1.knowledge}")
# print(f"Ready to work: {st1.ready_to_work}")
#--------------------------------------------------
# class Car:
#     def __init__(self,brand,model) -> None:
#         self.brand=brand
#         self.model=model
    
#     def show_info(self):
#         return f"{self.brand} -> {self.model}"
    
#     def __str__(self) -> str:
#         return self.brand +" " + self.model


# obj = Car("Audi","Q7")
# print(obj)
# car=Car("Lexsus","RX 330")
# print(car)
# print(obj.show_info())
#----------------------------------------------
# import random

# class Sniper:
#     health = 100

#     def __init__(self,name) -> None:
#         self.name=name

#     def shoot(self,other):
#         other.health -=20
#         print(f"Атаковал {self}")
#         print(f"У {other} осталось {other.health}")

#     def __str__(self) -> str:
#         return self.name
    
# sniper1 = Sniper("Friderih Sholtch")
# sniper2 = Sniper("DeadShot")
# while sniper1.health and sniper2.health:
#     chose = random.randint(1,2)
#     sniper1.shoot(sniper2) if chose==1 else sniper2.shoot(sniper1)

# if sniper1.health:
#     print(f"{sniper1} won the game!")
# else:
#     print(f"{sniper2} won the game!")
#--------------------------------------------------------------

# class Soda:
#     def __init__(self, ingredient = None):
#         if isinstance(ingredient, str):
#             self.ingredient = ingredient
#         else:
#             self.ingredient = None

#     def __str__(self) -> str:
#         if self.ingredient:
#             return (f"Gazirovka iz {self.ingredient}")
#         else:
#             return ("Defolt Gazirovka")

# a=Soda("Malina")
# print(a)

# b=Soda("5")
# print(b)

# c=Soda()
# print(c)

# d=Soda("Grusha")
# print(d)
#-------------------------------------------------
from typing import List

class TraingleCheker:
    def __init__(self,sides: List[int | float]) -> None:
        self.sides=sides

    def __str__(self) -> str:
        if not all(isinstance(x,(int,float)) for x in self.sides):
            return "Нелбзя построить треугольник! Invalid Value"
        elif any(x <= 0 for x in self.sides):
            return "Нелбзя построить треугольник! Invalid Value"
        elif self.sides[0]+self.sides[1]<= self.sides[-1]:
            return "Нелбзя построить треугольник! Invalid Value"
        else:
            return "Мы можем построить треугольник"
        
t1=TraingleCheker([10,10,10])
print(t1)

t2=TraingleCheker([-1,10,10])
print(t2)

t3=TraingleCheker([1,6,2])
print(t3)

t4=TraingleCheker([6,10,12])
print(t4)
