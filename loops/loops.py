# while <expression>:
    # <body>
# i=0
# while i<10:
#     i+=1
# print(f"цикл сработал {i} раз")

# ls=list(range(1,51))
# print(len(ls))
# while ls:
#     print(ls.pop(0))

# !!!личное наблюдение!!! while работает риверсивно

# name1=""
# name2=""
# i=0
# while name1.lower()!="john" and name2.lower()!="raychel":
#     name1=input("Vvedite imya: ")
#     nam2=input("Vvedite name2: ")
#     print()
#     if i>=3:
#         print("Цикл остановлен!")
#         break
#     i+=1

# else:
#     print("U got this! ")
# ---------------------------------------------------
# user={"username":"JohnSnow","password":"Ilovesmell",}
# i=3
# # password=""
# while password:=input(f"{user['username']} vvedite parol: ")!=user["password"]:
#     # password=input(f"{user['username']} vvedite parol: ")
#     i-=1
#     if i==0:
#         print("Vy zabaneni")
#         break

# else:
#     print("Parol vernii")

# ------------------------------------------------
# for <variable> in <iterable object>:
    # body
# lista=[0,1,2,3,4,5,6,7,8,9]
# i=iter(lista)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# import random
# ls=[]
# for i in range(1,101):
#     ls.append(random.randint(1,50))
# print(ls)
# print(len(ls))
# ls=set(ls)
# ls=list(ls)
# print(len(ls))
# print(ls)

# ls=["Sans","Pops","Asgor","Toriel","Frisk","Chara"]
# for i in ls:
#     if i =="Asgor":
#         continue # пропуск
#     print(f"Hello Mr/Miss {i}!")

# i=0
# while i<100:
#     i+=1
#     if i%2==0:
#         continue
#     print(i)


# d=100
# x=[]
# for i in range(1,int(d**0.5+1)):
#     if d%i==0:
#         x.extend({i,d//i})
# x.sort()
# print(x)