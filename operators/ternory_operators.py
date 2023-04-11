# sentence=input("Vvedite predlojenie: ")

# # if sentence[-1] == "?":
# #     print("Yes, voprositelnoe")
# # else:
# #     print("No, normal one!")

# print("Yes, voprositelnoe!" if sentence[-1]=="?" else "No, normal one!")

# ------------------------------------------------------------------------------
# Ternary operators(Тернарный оператор) - конструкция которая по своему действию аналогична if/else, но при этом записывается в одну строчку

# num1=int(input("Vvdite chislo: "))
# res="even number" if num1%2==0 else "odd number"
#     # even - четное                 odd number - нечетное
# print(res)

# <выражение если True> if <условие> else <выражение False>

# ls=[55,65,75,89,100,15,6]
# print(ls)
# ask=input("max or min: ")
# res=max(ls) if ask.lower()=="max" else min(ls)
# print(res)
# if ask.lower().strip()=="max":
#     print(max(ls))
# elif ask.lower().strip() == "min":
#     print(min(ls))
# else:
#     print("Invalid ask")
# res=max(ls) if ask.lower().strip()=="max" else min(ls) if ask.lower().strip()=="minqwe" else "Invalid ask"
# print(res)

# ------------------------------------------------------------------------------------
# flag=True
# symbols="0123456789"+'-'+'.'

# while flag:
#     print()
#     num1=input("Vvede pervoe chislo: ")
#     is_correct_number=1
#     for i in num1:
#         if i not in symbols:
#             print('Вы ввели неправильное число!')
            
#             is_correct_number=0
#             break
#     if not is_correct_number:
#         continue

#     num1=float(num1) if '.' in num1 else int(num1)
    
#     num2=input('Vvedite vtoroe chislo: ')
    
#     for i in num2:
#         if i not in symbols:
#             print('Вы ввели неправильное число!')
#             is_correct_number=0
#             break
#     if not is_correct_number:
#         continue

#     num2=float(num2) if '.' in num2 else int(num2)
#     operator=input("Vvedite operator(+,-,*,/): ").strip()
#     if operator=="+":
#         print(f"Result: {num1+num2}")
#     elif operator=="-":
#         print(f"Result: {num1-num2}")
#     elif operator=="*":
#         print(f"Result: {num1*num2}")
#     elif operator=="/":
#         if num2==0:
#             print("Impossible act!")
#         else:
#             print(f"Result: {num1/num2}")
#     else:
#         print("Wrong operator!")

#     choice=input("U want to continue?(yes/no): ").strip()
#     if choice.lower()!="yes":
#         flag=False
#         print("Bye bye!")

# ----------------------------------------------------------------------------------------
