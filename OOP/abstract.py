"""
Абстракция
"""
# Абстракция (Абстрактный класс) Принцип ООП, В котором создвется абстрактный класс (класс - пустышка) 
#В котором задаются названия аттрибутов и методов для того что бы мы могли их переопределить в дочерних классах
#(У нас есть название, но нет логики)

# from abc import ABC,abstractmethod,abstractproperty

# class AbstractAnimal(ABC):
    
#     @abstractmethod
#     def voice(self):
#         ...
# # abstractmethod - Декоратор который требует переопределние метода в наследуемом классе

#     @abstractproperty
#     def legs(self):
#         ...
# # abstractproprty - Декоратор который требует переопределения аттрибутов класса

# # obj = AbstractAnimal() #TypeError: Can't instantiate abstract class AbstractAnimal with abstract methods legs, voice

# # class Dog(AbstractAnimal):
# #     ...

# # obj = Dog() #TypeError: Can't instantiate abstract class AbstractAnimal with abstract methods legs, voice

# class Dog(AbstractAnimal):
#     legs = 4
    
#     def voice(self):
#         print("Гав Гав")
        
    

# obj = Dog() #TypeError: Can't instantiate abstract class Dog with abstract method legs
# print(obj.legs)
# obj.voice()
#-----------------------------------
# class Shape(ABC):
#     def __init__(self,name) -> None:
#         self.name = name

#     @abstractmethod
#     def area(self):
#         ...


# class Square(Shape):
#     def __init__(self, length) -> None:
#         self.length = length

#     def area(self):
#         return self.length ** 2

# obj = Square(12)
# obj.name
# print(obj.area())