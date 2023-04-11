# def add(num1: int, num2:int) -> int: 
#     return num1+num2
# def subtract(num1:int|float,num2:int|float) -> int|float:
#     return num1-num2
# def divide(num1:int|float,num2:int|float) -> int|float:
#     try:
#         return num1/num2
#     except ZeroDivisionError:
#         return "На ноль делить нельзя"
# def multiply(num1:int|float,num2:int|float) -> int|float:
#     return num1*num2
# def calculate(num1,num2):
#     """Наша функция выполняет арифметическую операцию"""
#     operator=input("Enter operator(+,-,*,/) ")
#     if operator=="+":return add(num1,num2)
#     elif operator=="-": return subtract(num1,num2)
#     elif operator=="*": return multiply(num1,num2)
#     elif operator=="/": return divide(num1,num2)
#     else: return "Вы ввели неверный оператор"
# def main():
#     num1=input("Enter first number: ")
#     num2=input("Enter second number: ")
#     try:
#         num1=float(num1) if "." in num1 else int(num1)
#         num2=float(num2) if "." in num2 else int(num2)
#     except ValueError:
#         print("You enter wrong number")
#         main()
#         return
#     while True:
#         result=calculate(num1,num2)
#         if type(result)==str:
#             print(f"Result: {result}")
#         else:
#             print(f"Result: {result}")
#             break 
#     question=input("You want to continue?(Yes/No)").lower().strip()
#     if question=="yes":
#         main()
#     else:
#         print("Thx for using our calculator")
    
# main()

