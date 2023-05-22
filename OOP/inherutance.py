# Принципы ООП
# 1.Наследование
# 2.Инкапсуляция
# 3.Полиморфизм

# 4.Абстракция
# 5.Композиции
# 6.Агрегация
#-------------------------------
# Наследование
# Позволяет принимать родительские методы и атрибуты дочернему классу

# Родительский класс
# Дочерний класс
#----------------------------------------
# class Animal:
#     def print_info(self):
#         print("I'm an Animal")

# class Lion(Animal):
#     pass

# class Dog(Animal):
#     pass

# lion=Lion()
# lion.print_info()
#----------------------------------------------
# class Animal:
#     def say(self):
#         print(f"This Animal name is {self.name}: {self.golos}")

#     def eat(self):
#         print(f"{self.name} eats: {self.meal}")

# class Lion(Animal):
#     name="Lion"
#     golos="Roar"
#     meal="Meat"
#     griva=True

#     def info(self):
#         print(f"{self.name} , griva: {self.griva}")

# class Dog(Animal):
#     name="Dog"
#     golos="Bark"
#     meal="Meat"
#     griva=False
#     def info(self):
#         print(f"{self.name} , griva: {self.griva}")

# class Coala(Animal):
#     name="Coala"
#     golos="roar"
#     meal="Efkalipt"
#     griva=False

#     def info(self):
#         print(f"{self.name} , griva: {self.griva}")

# rex=Dog()
# simba=Lion()
# julian=Coala()

# rex.say()
# rex.eat()
# print()
# simba.say()
# simba.eat()
# simba.info()
# print()
# julian.say()
# julian.eat()
#-------------------------------------
# class Person:
#     def info(self):
#         print("I'm person from Bishkek")

# class Student(Person):
#     def info(self):
#         super().info()
#         print("I'm study in Manas university")
    

# obj= Student()
# obj.info()
#------------------------------------------
# class Laptop:
#     def __init__(self,brand,model,price):
#         self.brand = brand
#         self.model = model
#         self.price = price

#     def get_info(self):
#         return {"brand": self.brand,"model":self.model,"price":self.price}

# class Acer(Laptop):
#     def __init__(self, model, price,year,videocard):
#         super().__init__("Acer", model, price)
#         self.year=year
#         self.video=videocard

#     def get_info(self):
#         repr= super().get_info()
#         repr["videocard"]=self.video
#         repr["year"]=self.year
#         return repr

# class Apple(Laptop):
#     def __init__(self, model, price,display,year):
#         super().__init__("Macbook", model, price)
#         self.display=display
#         self.year=year

#     def get_info(self):
#         repr= super().get_info()
#         repr["year"]=self.year
#         repr["display"]=self.display
#         return repr
    
# mac=Apple("Pro,",1500,14,2020)
# print(mac.get_info())

# acer=Acer("Swift",600,2019,"Nvidia")
# print(acer.get_info())
#----------------------------------------
class Employee:
    bonus = 1.5

    def __init__(self,name,salary) -> None:
        self.name = name
        self.salary=salary

    def get_info(self):
        return f"FIO {self.name}, Salary: {self.salary}"
    
    def gice_increase(self):
        self.salary *= self.bonus

    def __str__(self) -> str:
        return self.get_info()
    
class Developer(Employee):
    def __init__(self, name, salary,language) -> None:
        super().__init__(name, salary)
        self.lang=language

    def get_info(self):
        info=super().get_info()
        info += f" ,Prog Language: {self.lang}"
        return info

class Manager(Employee):
    def __init__(self, name, salary,devs=[]) -> None:
        super().__init__(name, salary)
        self.devs=devs

    def add_devs(self,developers):
        self.devs.append(developers)

    def show_devs(self):
        return [x.get_info() for x in self.devs]
    
dev1=Developer("Emir Sadiraliev",1500,"Python")
dev2=Developer("Mavlyan Faziliv",1200,"JAVA")
dev3=Developer("Ali Yakupov",1700,"C++")
dev4=Developer("Dinislam Shakirov",1300,"C#")

man1=Manager("Ilya Juravlev",4000,[dev1,dev2])
man2=Manager("Mars Stamkulov",1500)

print("Before")
print(f"Manager {man1}, has {man1.show_devs()} devlopers")
print(f"Manager {man2}, has {man1.show_devs()} devlopers")
man1.add_devs(dev3)
man2.add_devs(dev4)

dev3.gice_increase()
dev4.gice_increase()
man2.gice_increase()

print("After")
print(f"Manager {man1}, has {man1.show_devs()} devlopers")
print(f"Manager {man2}, has {man1.show_devs()} devlopers")