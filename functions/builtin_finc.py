
"""
встроенные функции 
"""
"""
Анонимные функции - lambda (Обычная функция с одной особенностью, у нее нет имени)
Принимает сколько угодно параметров, но всегда возврощяет одно выражение
"""

# def hello():
#     return 'hello'
# print(hello())

# x = lambda: 'hello'
# print(x())

# x = lambda a, b, c: (a * b) % c
# print(x(5, 5, 3))

# x = lambda num1, num2, degree=None: (num1 * num2) ** degree if degree else num1 * num2 
# print(x(2, 2, 3))
# print(x(5, 5))

# def myFunc(n):
#     return lambda num: num * n

# my_doubler = myFunc(2)
# print(my_doubler(50))

# list_ = ['hello', 'mil', 'john', 'daniel', 'vlad']
# a = sorted(list_, key=len, reverse=True)
# print(a)

# dict_ = {
#     'john': 500,
#     'tirion': 160_000,
#     'tom': 150,
#     'sanchar': 20,
#     'ayana': 100_000,
# }
# print(dict_.items())
# new_dict = dict(sorted(dict_.items(), key=lambda x: x [1], reverse=True))
# print(new_dict)

# dict_={
#     "john":500,
#     "tirion":160000,
#     "tom":150,
#     "sanjar":20,
#     "ayana":100000,
# }

# newdict=dict(sorted(dict_.items(),key=lambda x: x[1], reverse=True))
# print(newdict)

"""
map(function,iterable) - применяется к каждому элементу внутри iterable, которую мы ей передаем в function, 
закидывая в результат те данные, которые возвращает функция. В ркзултате мы получаем mapobject(iterator), в которм хранятся 
все наши данные.
"""


# ls=["1","2","3"]
# newlist=list(map(int,ls))
# print(newlist)

# ls=["john","aria","baku","bakberdi","lilo"]
# newlist=list(map(lambda x: "Hello mr/mrs " + x,ls))
# print(newlist)

"""
Функция высшего порядка - функция, которая принимает в качестве аргумента другую функцию
"""
"""
filter(function,iterable) - применяет ко всем элементам iterable функцию, которую мы передали и возвращает filterobject(итератор)
только с теми элементами, для которых функция вернула True
"""
# ls=["oleg","lili","one","billi","tirion"]
# newlist=list(filter(lambda x: "o" in x,ls))
# print(newlist)

"""
enumerate(iterable) - прнумировывает каждый элемент внутри iterable  ее собственным индексом
"""
# ls=["str1","str2","str3"]
# newlist=list(enumerate(ls))
# print(newlist)

"""
zip(iterables) - она соеденяет каждый элемент итерируемых объектов между собой в тип данных tuple 
и возвращает итератор
"""

# ls1=[1,2,3]
# ls2=[100,200,300]
# res=list(zip(ls1,ls2))
# print(res)

# ls1=[1,2,3,4,5]
# ls2=[100,200,300,400,500,600]
# ls3=[10,20,30]

# res=list(zip(ls1,ls2,ls3))
# print(res)

# "zip для создания словарей"

# d_keys=["hostname","location","vendor","model","IP"]
# data={
#     "octbr":["bishkek_octbr","Gorkaya 212","Vefa","Cisco","10.255.0.12"],
#     "1may":["bishkek_1may","Gogalya 12","Kampa","Cisco","11.352.2.16"],
#     "sverdl":["bishkek_sverdl","Mambetova 6","Frunze","Cisco","23.144.1.12"]
# }
# bishkek_data={}
# for k in data:
#     bishkek_data[k]=dict(zip(d_keys,data[k]))
# print(bishkek_data)

"""
all(),any()

all(iterable) - вовращает Trueб если все элемента итерируемого объекта истина,
иначе возвращает  False
"""
# ls=[5,6,7]
# print(all(ls))

# ip="10.255.0.155"
# ip1="10","125","0y","202"
# res=all(x.isdigit() for x in ip.split("."))
# print(res)

"""
any - Возвращает True, ечли хотя бы один элемент истинна
"""

# ls=[0,0,[],0]
# print(any(ls))

# ignore=["rm_rf","sudo","reset","poweroff"]
# command=input("Enter comand: ")
# if any(x for x in ignore):
#     raise Exception("Block u!")
# print("OK!")

# from random import choices
# from string import ascii_letters,digits
# from itertools import repeat

# symbols="_()+-@!#%"
# q_pass=int(input("Vvedite kol-vo paroley: "))

# res={
#     i(choices(ascii_letters,k=15),choices(digits,k=6),choices(symbols,k=2))
#     for i in repeat(lambda x,y,z:"".join(set(x+y+z)),q_pass)
# }
# print(res)
# print(f"Quantity of password: {len(res)}")

# from statistics import mean
# print(f"Avg len of passwords: {mean(len(x) for x in res)}")
# print(min(len(y) for y in res))