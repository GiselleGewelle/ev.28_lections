# Функция полиморфизм -> len():__len__
# print(len("Makers"))
# print(len([1,2,3,4,5]))
# print(len({1:2,3:4,5:6}))
#========================================================
# + (__add__) - метод полиморфизм
# print(5+5)
# print("lol" + "kek")
# print([1,2,3]+[4,5,6])
#===============================================================
# Полиморфизм - это способность функции(метода) использоваться для разных типов(классов)n
# Широко распрастраненное определние: "Один интерфейс - много реализаций"
# list.pop
# set.pop
# dict.pop
#=========================================================
# class Cat:
#     def __init__(self,name,age) -> None:
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"It's a cat. Cat name is {self.name}, age: {self.age}")
    
#     def make_sound(self):
#         print("Meow, Meow!")

# class Dog:
#     def __init__(self,name,age) -> None:
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"It's a dog. Dog's name is {self.name}, age: {self.age}")
    
#     def make_sound(self):
#         print("Bark, Bark!")

# cat = Cat("Garfild",5)
# dog = Dog("Pluto",6)

# for i in (cat,dog):
#     i.info()
#     i.make_sound()
#=========================================================
# from math import pi

# class Shape:
#     def __init__(self,name) -> None:
#         self.name = name

#     def area(self):
#         pass

#     def fact(self):
#         return f"Я фигура двумерной плоскости: {self.name}"
    

# class Square(Shape):
#     def __init__(self,length) -> None:
#         super().__init__("Квадрат")
#         self.length = length

#     def area(self):
#         return self.length ** 2

#     def fact(self):
#         return super().fact() + "\nУ квадрата все стороны равны и углы равны 90 градусам"
    

# class Circle(Shape):
#     def __init__(self, radius) -> None:
#         super().__init__("Окружность")
#         self.radius = radius
#     def area(self):
#         return pi * (self.radius ** 2)
    
# a = Square(8)    
# b = Circle(4)

# for i in (a,b):
#     print(i.fact())
#     print(i.area())

a = [1,2,3]
print(*a)
pass
