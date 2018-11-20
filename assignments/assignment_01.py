name = input('Enter your name: ')
age = input('Enter your age: ')

def get_decades(age):
    return("More than " + str(float(age) // 10) + " decades.")


def greetings(name, age):
    print("Hello " + name + ". I see that you're " + age + " years old." + get_decades(age))


def print_data(agr1, arg2):
    print("Args: ["+str(agr1)+", "+str(arg2)+"]")

greetings(name, age)
print_data(name, [float(age)])