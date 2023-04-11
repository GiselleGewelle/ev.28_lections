#Decorators
#Scope
#Built in functions

"""
Дектораторы - функция высшего порядка (функция которая принимает другую функцию в качестве аргумениа)
"""
# def sq(func):
#     def wrapper(num):
#         nums=func(num)
#         return list(map(lambda x:x**2,nums))
#     return wrapper
# @sq
# def func2(num):
#     return list(range(1,num,2))
# @sq
# def func(num:int):
#     return list(range(1,num))
# print(func(5))
# print(func2(8))

# def razbor(str1):
#     from string import punctuation,digits,ascii_letters
#     glas=[]
#     soglas=[]
#     symbols=[]
#     res={}
#     str1=str(str1)
#     str1=str1.strip().lower()
#     print(str1)
#     for i in str1:
#         if i =="а" or i =="я" or i =="е" or i =="ё" or i =="и" or i =="ы" or i =="ю" or i =="э" or i =="о" or i =="у":
#         #     glas.append(i)
#         # elif i =="А" or i =="Я" or i =="Е" or i =="Ё" or i =="И" or i =="Ы" or i =="Ю" or i =="Э" or i =="й" or i =="О" or i =="У":
#             glas.append(i)
#         elif i.isdigit() or i.isascii():
#             symbols.append(i)
#         else:
#             soglas.append(i)
#     res={"Гласные":len(glas),"Согласные":len(soglas),"Символы":len(symbols)}
#     return res
# print(razbor(""))

