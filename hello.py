
def greet_function(name:str,age:int) -> None:
    print(f"Hello, {name}! You are {age} years old.")


greet_function(input("Enter your name: "),int(input("Enter your age: ")))