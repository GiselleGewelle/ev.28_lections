"""ООП - объкутно ориентирование программирование"""

# Класс -> описание того как должен выглядеть объект,
# то есть в классе мы описываем какими свойствами должен обладать объект.

# Объект -> сущность которую мы сохдаем от класса, у объекта есть собственное состояние свойств(данных)

# целью создания было связать данные с функциями которые управляли этими данными

# Свойствами(аттрибутами) - называют обычные переменные внутри класса, в которых хранятся данные объекта

# Методы - это обычные функции внутри класса, методы описывают поведение объекта

#-------------------------------------------------------------------------------------------------------------

# class Human:
#     age=0
#     def __init__(self,first_name,last_name,job,citizenship):
#         self.name=first_name + " " + last_name
#         self.job = job
#         self.citizen = citizenship

#     def show_info(self):
#         return f"Name: {self.name}\njob: {self.job}\nage: {self.age}\ncitizen: {self.citizen}"
    
# dante=Human("Dante","Son of Sparda","Hunter","Vine")
# vergil=Human("Vergil","Son of Sparda","Surviver","Vine")

# print(dante.show_info())
# print()
# print(vergil.show_info())

# dante.age=40
# vergil.age=40
# print(dante.show_info())
# print(vergil.show_info())

#------------------------------------------------------------
# class Dog:
#     age=0
#     ear=True

#     def __init__(self,name,color):
#         "Инициализатор, именно здесь создаются аттрибуты объекта"
#         #self - Ссылка на объект который только что создался 
#         self.name=name
#         self.color=color

#     def bark(self):
#         print(f"{self.name} barking")
        
#     def show_info(self):
#         return f"Name: {self.name} color: {self.color} age: {self.age} ear: {self.ear}"

# brut = Dog("Brut","Brown")
# rex= Dog("Rex","Black")
# pitbull= Dog("Cutiepie","Gray")

# rex.age = 2
# brut.age = 10
# pitbull.age = 13
# brut.ear = False

# print(pitbull.show_info())
# print(brut.show_info())
# print(rex.show_info())
# brut.bark()
#---------------------------------------------------------------------------
class Human:
    def __init__(self):
        print("init worked!")
        self.raychel="Raychel"
        self.golod=100

    def eat(self,meal,finish=True):
        print(f'{self.raychel} покушала {meal}')
        if finish:
            self.golod -=50
        else:
            self.golod -=25


obj=Human()
print(obj.raychel,obj.golod)
obj.eat("burger",finish=False)
print(obj.raychel,obj.golod)
obj.eat("Kruasan",finish=True)
print(obj.raychel,obj.golod)

