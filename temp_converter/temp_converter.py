def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def main():
    while True:
        print("\n===Temperature Converter===")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Quit\n")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            c = float(input("Enter Celsius: "))
            print(f"{c}˚C = {c_to_f(c):.2f}˚F")
        elif choice == "2":
            f = float(input("Enter Fahrenheit: "))
            print(f"{f}˚F = {f_to_c(f):.2f}˚C")
        elif choice == "3":
            break
        else:
            print("Invalid option. Choose 1, 2, or 3.")
        
if __name__ == "__main__":
    main()