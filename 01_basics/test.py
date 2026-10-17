import math

class Fruits:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    def intro(self):
        return f"my name is {self.name} and Type is {self.type}"

    def intro1(self):
        return self.intro()


apple = Fruits("Apple", "Sweet")

print(apple.intro1())

####################################

user={
    "name": "Vivek",
    "age": 29,
    "courses": ["React.js", "Node.js", "AWS"]
}

user["city"] = "Jamshedpur"

print(user)

userCourses = user["courses"]

for x in userCourses:
    print(x)

for i in range(0, len(userCourses)):
    print(i, userCourses[i])
    if userCourses[i] == "Node.js":
        print(f"Enrolled couse is: {userCourses[i]}")

    match userCourses[i]:
        case "AWS":
            print(f"Enrolled course is: {userCourses[i]}")
        case "React.js":
            print(f"Enrolled course is: {userCourses[i]}")
        case _:
            print("=== NOT AWS/React.js ===")

def add(a,b):
    return a + b

print(add(5, int("10")))