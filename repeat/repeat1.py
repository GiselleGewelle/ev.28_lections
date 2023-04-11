# num1=1

# while num1>=0:
#     num1=input("vvedite chislo:")
#     if num1[0]=="-" and num1[1:].isdigit():
#         num1=int(num1)
#     else:
#         num1=1

# print("vstretilos - chislo")

# from random import randint
# ls=[]
# for i in range(0,100):
#     ls.append(randint(0,100))
#     ls.sort()
#     # print(ls,len(ls)) 

#     res=[]
#     for i in ls:
#         if i not in res:
#             res.append(i)
# print(res,len(res))

# x1=int((input("vvedite 1 kordinatu gde stoit ladya")))
# y1=int((input("vvedite 2 kordinatu gde stoit ladya")))
# ladya=[x1,x1]

# x2=int(input("vvedite 1 coordinatu kuda idet ladya:"))
# y2=int(input("vvedite 1 coordinatu kuda idet ladya:"))
# target=[x2,y2]

# if x1==x2 or y1==y2:
#     print(True)
# else:
#     print(False)

# import random
# ls=["Plov","BeshBarmak","Kuurdak","Oromo","Lagman"]
# p=0
# b=0
# k=0
# o=0
# l=0
# for i in range(1,1000000):
#     meal=random.choice(ls)
#     # print(meal)
#     if meal.lower()=="plov":
#         p+=1
#     elif meal.lower()=="beshbarmak":
#         b+=1
#     elif meal.lower()=="kuurdak":
#         k+=1
#     elif meal.lower()=="oromo":
#         o+=1
#     elif meal.lower()=="lagman":
#         l+=1
# print("resultati golodnih igr:")
# print(f"Plov{p}\nBeshBarmak{b},\nKuurdak{k}\nOromo{o},\nLagman{l}")
# if p>b and p >k and p>o and p>l:
#     print(f"Победитель:\n {p}")
# if p>b and p >k and p>o and p>l:
#     print(f"Победитель:\n {p}")
# if p>b and p >k and p>o and p>l:
#     print(f"Победитель:\n {p}")
# if p>b and p >k and p>o and p>l:
#     print(f"Победитель:\n {p}")
# if p>b and p >k and p>o and p>l:
#     print(f"Победитель:\n {p}")
# if p>b and p >k and p>o and p>l:
#     print(f"Победитель:\n {p}")

# ---------------------------------------------------------------------------------------

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# nums=[1,2,13,15,22]
# target=35
# for i in range(0, len(nums)):
#     num=target-nums[i]
#     if num in nums:
#         print(f"Otvet: {i} {nums.index(num)}")
#         break