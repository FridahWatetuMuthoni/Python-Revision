def main():
    name, house = get_student()
    print(f"Name:{name} House:{house}")


def get_student():
    while True:
        name = input("Enter name: ")
        house = input("Enter house: ")
        
        if(name.strip() and house.strip()):
            return (name, house)

if(__name__ == "__main__"):
    main()