# операторы сравнения
# >,<, ==, !=, <=,>=
# условные операторы и логические операторы

# условные операторы
# if
# elif
# else
# if<condition>:
#     <body> - сработает если в condition if придет True
# [elif]<condition>:
#     <body elif>
# else:
#     <body else> - сработает если во всех вышестоящих условиях пришло False

# string=input("Enter smt: ")
# if string.lower()=="hello":
#     print("Hello, it's me \nI was wondering if after all these years you'd like to meet")
# elif string.lower()=="john":
#     print("It's you again?")
# elif string.lower()=="imposible":
#     print("why this is imposible?")
# else:
#     print("Not for you!")

# print("Registratiom Form: ")
# email=input("Enter email: ")
# password=input("Enter the Pasword")
# if len(password)< 8:
#     raise ValueError("Password is too short!\nNeed to be 8 or more sybols")
# elif password.isdigit():
#         raise ValueError("Password is invalid\nPassword must contian symbols too!")
# elif password.isalpha():
#         raise ValueError("Password is invalid\nPassword must contian number or special symbols too!")

# password2=input("Enter Password again: ")
# if password2!= password:
#     raise ValueError("Passwords did not match")
# else:
#     print(f"successfuly registered! Hello mr/mrs {email}!")

# age=input("Enter youre age:")
# if age.isdigit():
#     age=int(age)
# else:
#     raise ValueError("Enter only numbers")
# if age<18:
#     print(f"Access DEnied! Come again after {18 - age} years!")
# else:
#     print("you can pass! Welcome to the club body")

# and - и
# or - или
# not - отрицание

# money=input("Vvedite wash balans")
# status=input("vvedite kakoy u was status\n 'base'\n'premium'\n")

# if int(money)>1_000_000 and status == "premium":
#     print("you're president of our club")
# elif int(money) > 1_000_000 or status == "premium":
#     print("you're ministr of our club")
# else:
#         print("you're defolt member of our club")

# str1="hello world"
# print(str1)
# symbol=input("enter the symbol:")

# if symbol not in str1:
#     print(f"the symbol {symbol} does not exisit")
# else:
#     print(f"the symbol {symbol} exisit")


# разрешаем доступ если он юзер гита или гугла и его возраст больше 21 или у него баллы(10000)

# user="John"
# is_google_user=True
# is_github_user=False
# age=19
# user_coins=9000

# if (is_google_user or is_github_user) and (age >21 or user_coins >10000):
#     print(f"you can enter the system Mr/Mrs {user}")
# else:
#     print("Sorry Bro, I cant put you in")







