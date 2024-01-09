def main():
    students = []
    for _ in range(5):
        print("Enter Student Details:")
        student = get_student().get_student()
        students.append(student)
    print(students)
    


class Student:
    school = "Havard University"
    
    def __init__(self, name, house):
        self.name = name 
        self.house = house
    
    def get_info(self):
        return f"{self.name} is in {self.house}"
    
    def get_school(self):
        return f"You are in {Student.school}"
    
    def get_student(self):
        student = {
            "name" : self.name,
            "house" : self.house
        }
        return student


def get_student():
    while True:
        name = input("Enter name: ")
        house = input("Enter house: ")
        
        if(name.strip() and house.strip()):
            student = Student(name, house)
            return student


if __name__ == "__main__":
    main()