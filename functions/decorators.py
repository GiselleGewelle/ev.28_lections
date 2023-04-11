# Декораторы - функция, которая позволяет без изменения кода функции расширить ее функционал


# def decorator(func):
#     print(func)
#     func()
# def hello():
#     print("Hello stranger!")
# def john():
#     print("My name is John!\nI am king of north!")
# decorator(hello)
# print("----------------------------")
# decorator(john)
# pythonic way -> @
# Синтаксический сахар
# def decorator(func):
#     def wrapper():
#         print(f"Мы вызвали функцию {func.__name__}")
#         func()
#     return wrapper

# @decorator #@decorator->decorator(hello)
# def hello():
#     print("Hello stranger!")

# @decorator
# def john():

#     print("My name is John!\nI am king of north!")

# hello()
# print()
# john()
# def benchmark(func):
#     def wrapper(*args,**kwargs):
#         import time
#         start=time.time()
#         func(*args,**kwargs)
#         finish=time.time()
#         print(f"Время выполнения функции {func.__name__}, заняло: {finish-start}")
#     return wrapper

# @benchmark
# def loop():
#     i=0
#     range_number=1000000
#     while i < range_number:
#         i+=1
# @benchmark
# def add():
#     i=0
#     range_number=10000000
#     ls=[]
#     while i<range_number:
#         ls.append(i)
#         i+=1
# loop()
# add()

# def bold(func):
#     def wrapper(*args,**kwargs):
#         res="<bold>" + func(*args,**kwargs)+ "</bold>"
#         return res
#     return wrapper

# def div(func):
#     def wrapper(*args,**kwargs):
#         res="<div>" + func(*args,**kwargs)+"</div>"
#         return res
#     return wrapper

# @div
# @bold
# @div
# def str1(name):
#     return name
# print(str1("Abdusattar"))

#---------------------------------------------------
# def trace(func):
#     def wrapper(*args,**kwargs):
#         print(f"Trace: вызвала {func.__name__}()\nона приняла args: {args}, kwargs{kwargs}")
#         original_result=func(*args,**kwargs)
#         print(f"Trace: Вызвала {func.__name__}()\nота вернула: {original_result}")
#         return original_result
#     return wrapper

# @trace
# def say(name,address):
#     return f"{name} ==> {address}"

# @trace
# def hello(name,last_name,country):
#     return f"Hello {name} {last_name} from {country}"

# print(say("Sherlock","Bakery street 221B"))
# print()
# print(hello("homer","Simpson","USA"))
