# list comprehensions - генераторы списков

# list comprehensions - упрощенный подхрд к созданию списков, который задействует цикл for, 
# а так же конструкцию if, для определения того, ято ы итоге попадет в наш список

# list - > 0-200 -> num%2==0
# ls=[]
# for x in range(0,201):
#     if x%2==0:
#         ls.append(x)

# ls=[x for x in range(0,201) if x%2!=0]
# print(ls)

# list:0-300 -> num%2==0 and num%3==0

# ls=[x for x in range(0,301) if x%2==0 and x%3==0]
# print(ls)

# ls=[i**2 if i%2==0 else i**3 
#     for i in range(0,101) 
#     if i%2==0 or i%3==0]
# print(sorted(ls))

#----------------------------------------------------------------------------------------------------------------
# newList=[expression for item in iterable <if comditiom == True> ]

# ls=[str(i*2) for i in range(0,11)]
# print(ls)

# ls=[[1,2,3],[4,5,6],[7,8,9]]
# result=[j for i in ls for j in i ]
# # for i in ls:
# #     for j in i:
# #         result.append(j)
# print(result)

#    /\         |-------|
#   /  \        |       |
#  /    \       |       |
# /______\      |-------|
# from datetime import datetime
# start=datetime.now()
# ls =[i for i in range(0,100000000)]
# # for i in range(0,100000000):
# #     ls.append(i)
# finish=datetime.now()
# print(finish-start)
#----------------------------------------------------------------------------------------------
#set compehensions
# seto={i for i in range(1,100)}
# print(seto,type(seto))
#-----------------------------------------------------------------------------------------------
# dict compehensions
# dict{
#     key:value,
#     keyLvalue,
# }

# dicty={i:i**2 for i in range(0,16)}
# # print(dicty)
# names=["Sans","Pops","Asriel","Toriel","Asgor"]
# dicty={i:len(i) for i in names}
# print(dicty)

# ----------------------------------------------------------------------------------------------
# import itertools


# dict1={"Soke":{"history":99,"fizik":95,"math":94},
#        "Omoke":{"history":84,"fizik":86,"math":68},
#        "Ralf":{"history":90,"fizik":90,"math":100},}
# dict2={}
# for key,value in dict1.items():
#     # print(key)
#     # print(values)
#     for innerkey,innervalues in value.items():
#         if max(value.values())==innervalues:
#             dict2[key]=innerkey
# print(dict2)
# dict1={"Soke":{"history":99,"fizik":95,"math":94},
#        "Omoke":{"history":84,"fizik":86,"math":68},
#        "Ralf":{"history":90,"fizik":90,"math":100},}
# dict2={key:innerkey for key,value in dict1.items() for innerkey,innervalue in value.items() if innervalue==max(value.values())}
# print(dict2)
