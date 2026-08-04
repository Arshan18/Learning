def avg():
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    average = (a + b) / 2         
    print(average)

avg()


def greet(name):
    gr = "Hello" + " " + name
    return gr

a = greet("Harry")
print(a)

def day(name, ending = "Thanks"):
    print(f"Good Day, {name}")
    print(ending)

day("Sam")