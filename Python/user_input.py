def user_input(_name, _age, _location):

    return f"Hello {_name}, you are {_age} years old and live in {_location}"


if __name__ == "__main__":
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    location = input("Enter your location: ")
    print(user_input(name, age, location))
