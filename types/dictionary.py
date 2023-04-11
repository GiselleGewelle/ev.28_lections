# dict() - словарь -> упорядоченная коллекция элементов (python 3.7 -> ordered). 
# Каждый элемент внутри словаря хранится в виде пары {ключ:значение}
# ассоциативный массив, hash table, object(js),structure == dictionary(py)

# ключами могут быть только неизменяемые типы данных и в словаре сохраняются только уникальные ключи.
# тогда как значениями могут выступать любые типы данных
 
# thisdict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":"1967"
# }
# print(thisdict)
# print(type(thisdict))
# print(thisdict["model"],thisdict["brand"])
# print(thisdict["year"])

# thisdict["motor"]="GTE turbo"
# thisdict["brand"]="Tesla"
# print(thisdict)

# a={}
# b=dict()
# print(type(a))

# ----------------------------------------------------------

# print(dir(dict))

# items,keys,values

# userInfo={
#     "Name":"Giselle",
#     "LastName":"Gewelle",
#     "age":20,
#     "email":"satavamas@mail.ru",
#     "role":"admin"
# }
# ls=userInfo.keys()
# ls=list(ls)
# ps=userInfo.keys()
# ps=list(ps)
# kpss=userInfo.items()
# print(kpss)
# print(ls[2:])
# print(ps)
# for key,value in userInfo.items():
#     print(f"keys: {key}, values: {value}")

# dict_={"name":"jack","age":17}
# print(dict_)
# dict_["name"]="john"
# dict_["age"]=24
# dict_["plade"]="WinterFell"
# print(dict_)
# dict_.update({"age":25,"place":"BlackCastle"})

# ----------------------------------------------------------
# получение даннх со словоря
# dicty={1:"Pizza",2:"Burger",3:"Steak"}
# print(dicty[2],"!!!")
# print(dicty.get(2))

# setdefault() - работает как get но если нет такого ключа, создает новую пару

# dicty={1:"Pizza",2:"Burger",3:"Steak"}
# print(dicty.setdefault(4,"Manty"))
# print(dicty)

# создание - fromkeys
# ls=list(range(1,100))
# newDict=dict.fromkeys(ls,'value')
# print(newDict)

# ------------------------------------------------------------------------
# удаление элементов 
# pop, popitem

# pop(<key>) - удаляет пару по ключу

# dicty={"name":"John","LastName":"Snow"}
# print(dicty)
# removed=dicty.pop("LastName")
# print(dicty)
# print(removed)

# popitem - удаляет последнюю пару

# dicty={"name":"John","LastName":"Snow"}
# removed=dicty.popitem()
# print(dicty)
# print(removed)

# -----------------------------------------------------------------------
# roles={
#     0:"admin",
#     1:"customer",
#     2:"vendor",
# }

# users={
#     1:{
#     "id":1,"role":roles[2],"username":"Tirion",
#     },
#     2:{
#     "id":2,"role":roles[0],"username":"John"
#     },
#     3:{
#     "id":3,"role":roles[1],"username":"Ronald",
#     },
# }
# print(users)
# product={
#     "id":1,
#     "title":"Samsung Galaxy A51",
#     "description":"Lorem Ipsum",
#     "price":250,
# }
# print(product)
# idUser=int(input("Vvedir ID: "))
# if users[idUser]["role"]==roles[0]:
#     product["description"]=input("Vvedite opisanie")
# else:
#     print("You do not have permissions")

# print(product)
# string="1#2#3#1#2#3"
# string=string.split("#")
# if string.isdigit():
#     x=int(string[0])+int(string[1])+int(string[2])
#     y=int(string[3])+int(string[4])+int(string[5])
#     if x==y:
#         print("да")
#     else:
#         print(x,y)
#         print("нет")
# else:
#     print("")

