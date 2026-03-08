from math import *

def main():
    while True:
        print("=" *44 + "\n\tCALCULATOR BY JADON SAMUEL\n" + "=" * 44, end="\n\n")
        num1 = input("Enter your first number: ")
        op = input("Enter operator: ")
        while op not in ["+", "-", "/", "*"]:
            op = input("Enter valid operator: ")
        
        num2 = input("Enter your second number: ")
        
        res = eval(f"{num1} {op} {num2}")
        print(f"Result: {res}")
        
        cont = input("Would you like do another calculation?: ")
        if cont.lower() == "no":
            break

main()