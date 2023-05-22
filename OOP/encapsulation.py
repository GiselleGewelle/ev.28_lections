# Инкапсуляция: 
# 1. Языкавая конструкция, которая помогает связать данные с их методами для их обработки и управления
# (свяхь между данными и методами которые управляют ими)
# (Класс - капсула)
# 2. Механизм сокрытия, при помощи которого можно ограничить доступ одного компонента программы к другому'

# Инкапсуляция как связь

# class Phone:
#     number="+996707667742"

#     def print_number(self):
#         print(f"мой номер: {Phone.number}")
#         print(f"мой номер: {self.number}")

# my_phone=Phone()
# my_phone.print_number()

# Инкапсуляция как механизм сокрытия
# 3 Уровня сокрытия данных:
#     1.публичный(public) - number,print_number
#     2.защищенные(_protected) - _number
#     3.Приватный(__private) - __number

# class Car:
#     _country="Germany"
    
#     def __init__(self) -> None:
#         self.marka= "Mecedes-Benz" #public
#         self._model="w140"  #_protected
#         self.__color = "gray"

# obj = Car()
# print(dir(obj))
# print(obj.marka)
# print(obj._country)
# print(obj._Car__color)

# class Phone:
    # username = "John"
#     caller = "Jamie"
#     count_of_calls = 15
    
#     def call(self):
#         print(f'{self.caller} звонит вам!')
#         question = input("Взять трубку (yes/no): ")
#         if question.lower().strip() == 'yes':
#             self.__turn_on()
#         else:
#             print('Сборсили трубку!')

#     def __increment_calls(self):
#         self.count_of_calls += 1
    
#     def __turn_on(self):
#         self.__increment_calls()
#         print("Hello?")
#         print(f"Count of calls with {self.caller} {self.count_of_calls}")

# john=Phone()
# john.call()
# john.call()
# john.call()
# john.call()

#-------------------------------------
# class Person:
#     def __init__(self,name, age) -> None:
#         self.name = name 
#         self.age = age

#     def display_info(self):
#         print(f"My name is {self.name} and I'm {self.age} years old")

# obj = Person("John",18)
# obj.display_info()
# obj.name = "Luca Changrete"
# obj.nationality = "Italian"
# print(dir(obj))
# obj.display_info()

#-----------------------------------------------------------
# getter & setter
# Они нужны чтобы избежать прямого обращения к сокрытым атрибутам при этом можно 
# добавить логику валидации(проверки) данных которые будут установленны в атрибут

class Person:
    def __init__(self,name, age) -> None:
        self.__name = name 
        self.__age = age
        
    def display_info(self):
        print(f"My name is {self.__name} and I'm {self.__age} years old")

    #getter
    def name(self):
        return self.__name
    
    #setter
    def set_name(self,name):
        if not isinstance(name,str):
            print("Name must be str object")
        else:
            self.__name=name

    def get_name(self):
        return self.__age
    
    #setter
    def set_name(self,age):
        if not isinstance(age,int) or not 0 <=age <=122:
            print("Invalid value")
        else:
            self.__age=age
#_______
# |0.0|
#  \-/

obj = Person("John",24)
print(obj.name())
obj.set_name(-18)
