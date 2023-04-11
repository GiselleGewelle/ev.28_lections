# обработка исключений
# операотры try..except
# Errors -> связаны с кодом
    # SyntaxError
    # IndentationError
    # TabError

# исключения exceptions -> связаны с неправильными данными которые передаются в код
    # ZeroDivisionError
    # ArithmeticError
    # NameError
    # IndexError
    # KeyError
    # ValueError
    # BaseException - прародитель всех исключений
# try:
#     a=int(input("Enter the number"))
# except:
#     print("incorrect value")
# else:
#     print(a*5)

# try:
#     <body>
# except:
#     <body> - если есть ошибка
# else:
#     <body> - если нет ошибки   -----------
# finally:                                 |--- необязательные 
#     <body> - работает в любом случае------

# ls=["lol","kek","lmao"]
# try:
#     i=int(input("Enter index: "))
#     print(ls[i])
# except ValueError:
#     print("u enter wrong value!")
# except IndexError:
#     print("u enter wrong index!")
# ---------------------------------------------------------------------------------
# отображение ошибки 
# Exception as e (error)

# dicty={1:"one","2":"two","name":"Lol"}
# try:
#     key=int(input("Enter key: "))
#     print(dicty[key])
# except Exception as e:
#     print(f"Oops {e.__class__}error")

# try:
#     num1=int(input("Enter num1: "))
#     num2=int(input("Enter num2: "))
#     res=num1/num2
# except ValueError:
#     print("Invalid input!")
# except ZeroDivisionError:
#     print("delit na - nelzya!")
# else:
#     print(res)
# finally:
#     print("The end!")