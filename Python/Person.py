class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f"The person's name is {self.name}, age is {self.age} and gender is {self.gender}")
        

if __name__ == "__main__":
    p = Person("John", 25, "male")
    p.display()