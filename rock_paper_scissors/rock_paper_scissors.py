import random
import time

def main():
    while True:
        print("=" * 51 + "\n\tROCK PAPER SCISSORS BY JADON SAMUEL\n" + "=" * 51, end="\n\n")
        user = input("Pick your choice. Rock (r), paper (p), scissors (s): ")
        while user not in ["r","p","s"]:
            user = input("Pick your choice. Rock (r), paper (p), scissors (s): ")
        computer = random.randint(1,3)
        
        print("Ready?")
        time.sleep(1)
        print("Rock! ", end=" ", flush=True)
        time.sleep(0.5)
        print("Paper! ", end=" ", flush=True)
        time.sleep(0.5)
        print("Scissors! ", end=" ", flush=True)
        time.sleep(0.5)
        print("SHOOT!!!")
        
        match computer:
            case 1:
                if user == "r":
                    print("Tie game.")
                elif user == "p":
                    print("You Won. Paper beats rock")
                elif user == "s":
                    print("You Lost. Rock beats scissors")
            case 2:
                if user == "r":
                    print("You Lost. Paper beats rock")
                elif user == "p":
                    print("Tie game.")
                elif user == "s":
                    print("You Won. Scissors beats paper")
            case 3:
                if user == "r":
                    print("You Won. Rock beats scissors")
                elif user == "p":
                    print("You Lost. Scissors beats paper")
                elif user == "s":
                    print("Tie game:")
        
        again = input("Play Again? (y/n): ")
        if again == "n":
            break

if __name__ == "__main__":
    main()