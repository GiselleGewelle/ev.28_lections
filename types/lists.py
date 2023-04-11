# list() -> (списки,массив) - Это изменяемый последовательный тип данных который 
# пердставляет из себя коллекцию каких либо объектов(значения)
# my_list=[1,2,"string",False,None,[1,2,3,4,5]]
# print(my_list,type(my_list))

# range() - возвращает последовательность элементов (чисел)
# ls=range(1,101)
# myList=list(ls)
# print(myList)

# list()

# my_list=list("hello world")
# print(my_list)

# tuple_=("banana","apple","Cherry")
# print(tuple_,type(tuple_))
# ls=list(tuple_)
# print(ls,type(ls))

# индексация в списках
# ls = [1,2,3,4,5,"hola",[True,False,None]]
# print(ls,len(ls))
# print(ls[1],ls[2])
# print(ls[4:])
# print(ls[6][2])

# ls=list(range(1,21))
# print(ls)
# for i in ls:
#     if i%2==0:
#         print(pow(i,2))
#     elif i%2!=0:
#         print(pow(i,3))

# # ls=["John","Sans","Papyrus","Asgor","Frisk"]
# print(ls,len(ls))
# for i in ls:
#     print(f"Hellos Mr/Mrs {i}! Welcome to the club body!")

# ----------------------------------------------------------------------------------
# методы списков

# print(dir([]))

# append(element) - добавляет элемент в конец списка(принимает 1 элемент за раз)

# ls=[1,2,3]
# ls.append(4)
# ls.append(5)
# ls.append("hello")
# ls.append([1,2,3,4])
# print(ls)

# extend(onject) - расширяет список
# ls =[1,2,3]
# ls.append("hello")
# print(ls)
# plea=[1,2,3,4,5,67]
# ls.extend(plea)
# print(ls)

# sort() - сортирует список, если передать reverse=True , то список отсортируется в порядке убыванмя
# from random import randint
# ls=[]
# for i in range(0,100):
#     num=randint(0,1000)
#     ls.append(num)
# print(ls)
# ls.sort(reverse=True)
# print("After:")
# print(ls)

# ls=["sans","pops","asgor","flowy"]
# ls.sort(key=len,reverse=True)
# print(ls)

# insert(index,element) - добавляет элемент по указанному index
# ls=["string:",2,3,False]
# ls.insert(0,1)
# print(ls)

# remove(element) - удаляет элемент из списка, если такого нет выводит ошибку
# pop(index)- удаляет и возвращает элемент из списка по индексу, но если индекс не передать то удаляет последний элемент
# ls =[5,1,2,3,4,5,5,5]
# # ls.remove(5)
# # print(5 in ls)
# while 5 in ls:
#     ls.remove(5)
# print(ls)

# ls=[5,2,3,4,5,5,5]
# # print(ls.pop(0))
# # print(ls.remove(5))
# deleted=ls.pop()
# print(ls)
# print(deleted)

# update-----------------------
# ls=[1,"h",3]
# print(ls)
# ls[1]=2
# print(ls)
# ls.reverse()
# print(ls)
# print(ls[::-1])

# pizza=["first","second","third","fourth","fifth","sixth"]
# spisok=[]
# for i in pizza:
#     if not i.startswith("f"):
#         spisok.append(i)

# print(spisok)
# x=int(input)
# if x>12:
#     print("Такого месяца нет")
# elif x==1 or x==2 or x==12:
#     print("зима")
# elif x==3 or x==4 or x==5:
#     print("весна")
# elif x==6 or x==7 or x==8:
#     print("лето")
# elif x==9 or x==10 or x==11:
#     print("осень")