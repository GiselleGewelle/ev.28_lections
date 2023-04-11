# set() - Множества 
# Это изменяемый неупорядоченый, итерирумый неиндексируесмый тип данных

# множества хранят в себе тольео неизменяемые типы даных

# print(hash("lolipop"))
# 1 -> set
# a=set([1,2,3,4,5])
# print(a)

# a=set({1:2,3:4})
# print(a)

# 2 -> {}
# set2={1,2,3,4,2,1}
# print(set2)4
# set1={1,3,True,False}
# print(set1)

# Методы set
# add() -> для добавления в конец
# set1={1,2,3}
# set1.add(4)
# print(set1)
# set1.add((1,2,3,4,5))
# set1.add((1,2,3,4,5,7))
# print(set1)

# update() -> Он может добавлять несколько значений разом не повтаряя имеющиеся и добавляет все итерируемые
# set1={1,2,3}
# set1.update("string",{1,2,3,4,5,6,7,8})
# set1.update([1,2,3,4,5,1,1,42])
# print(set1)

# удаление в set

# clear - очищает все множества
# remove(element) - удаляет заданный элемент
# discard(element) - тот же remove но не выдает ошибку
# pop() - удаляет из set(FIFO) first in first out
# set1={1,2,3,4,5}
# set1.pop()
# print(set1)

# # difference - выводит отличия
# set1={1,2,3,4,5}
# set2={2,3,6,8,9}
# # # print(set1.difference(set2))
# # print(set2 - set1) # тот же difference
# # a=set1.symmetric_difference(set2)
# # print(a,type(a))
# # print(set1^set2) # тот же difference
# # set1.symmetric_difference_update(set2) - обновляет set1
# print(set1)
# print(set1.intersection(set2))
# print(set1&set2) тот же intersection
# print(set1.union(set2)) # Объеденяет set1 and set2
# print(set1|set2) # Union too

# set1=set(["White","Black","Red"])
# set2=set(["Green","Red"])
# print(set1 - set2)

# num=list(input())
# print(len(num)==len(set(num)))

# frozenset неизменяемое множество
# a=frozenset([1,2,3,4,5,6])
# print(a)

# tuple - неизменяемый, индексируемый, итерируемый, упорядоченный тип данных index(element) - возвращает индекс этого элемента в кортеж
# литералы ()
# a=(True,False,1,2,3,"LOL","Kefteme",1,1,1,1)
# # c=()
# # print(c,type(c))
# # print(a,type(a))
# # count(element) - считает кол-во вхождений элемента в кортеж
# print(a.count(True))


# a=int(input())
# b=int(input())
# c=int(input())
# x=b
# b=min(a,b,c)
# a=max(a,b,c)
# c=sum([a,x,b])-max(a,x,b)-min(a,x,b)
# if (c**2)+(b**2)==(a**2):
#     print("rectangular")
# elif a+b<=c or a+c<=b or b+c<=a and (a**2)>(b**2)+(c**2):
#     print("obtuse")
# elif a+b<=c or a+c<=b or b+c<=a and (a**2)<(b**2)+(c**2):
#     print("acute")
# elif a+b<=c or a+c<=b or b+c<=a or a==0 or b==0 or c==0:
#     print("impossible")