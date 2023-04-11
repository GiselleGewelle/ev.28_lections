# list1="Hello world! My name is John, last name is Snow. Nice to meet you!"

# def reversiv(list1):
#     rever=list1.split(" ")
#     list2=rever[::-1]
#     return " ".join(list2)
# print(reversiv(list1))

# def sum_of_args(a,b,c=5,d=5): # параметры
#     return a+b+c+d
# resilt=sum_of_args(1,2,3,4) # аргументы
# print(resilt)
# res=sum_of_args
# print(res,type(res))
# print(res(5,6,7,8))
# print(res(5,5))

#----------------------------------------------------------------------------

# позиционные и именованные аргументы

# def printParams(a,b,c):
#     print(a,"is sorted in param a")
#     print(b,"is sorted in param b")
#     print(c,"is sorted in param c")
# printParams(5,10,15)
# print()
# printParams(c=5,b=15,a=10)

# def sum_of_args(a,b,c,d): # параметры
#     return a+b+c+d
# print(sum_of_args(5,10,15,20)) #arguments (posicionnie argumenti)
# print(sum_of_args(a=5,c=20,b=10,d=15)) # keyword argumetns(imenovanie argumenti)
# print(sum_of_args(5,10,c=15,d=20))

#-----------------------------------------------------------------------------------------------------
# operator *
# a=[1,2,3]
# b=[4,5,6]
# c=[*a,*b] 
# print(c)
#---------------------------------------------------
#*args,**kwargs in func

# def printScores(student,*args):
#     print(f"Name of studebt: {student}")
#     # print([*args])
#     print(f"Avarage: {sum(args)/len(args)}")
#     for i in args:
#         print("Scores:",i)
#     return
# printScores("John Snow",100,90,80,95,88)

# def printPetNames(owner,**pets):
#     print(f"Ownwr name: {owner}")
#     # print(pets)
#     for pet,name in pets.items():
#         if type(name)==list:
#             print(f"{pet}: ",*name)
#         else:
#             print(f"{pet}: {name}")
# printPetNames("John snow",dog="Pluto",cat="Garfild",fish=["Nemo","Dori","Batya"],turtle="Mikilyanjelo")

# def get_some_data(a,b,*args,**kwargs):
#     print("параметры a и b: ",a,b)
#     print("аргументы: ",args)
#     print("именованные аргументы: ",kwargs)

# get_some_data(1,2,3,4,5,lang="python",car="audi")


# def generate_random_password(len_):
#     import string as s
#     import random 
#     # print(s.ascii_letters,s.digits,s.punctuation)
#     symbols=s.ascii_letters + s.digits
#     res=list(
#        random.choice(symbols) for i in range(1,len_)
#     )+ list(random.choice(s.punctuationlist_ = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]))
#     random.shuffle(res)
#     return "".join(res)
# print(generate_random_password(8))
