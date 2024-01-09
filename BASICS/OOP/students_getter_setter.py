class Student:
    def __init__(self, name, house):
        self.name = name 
        self.house = house
        
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    #Getter
    @property
    def house(self):
        return self._house
    
    #setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("The name should not be empty")
        self._name = name


def main():
    student = get_student()
    print(f"{student.name} in {student.house}")


def get_student():
    name = input("Enter Name: ")
    house = input("Enter House: ")
    try:
        student = Student(name, house)
        return student
    except ValueError as error:
        print(error)

if __name__ == "__main__":
    main()