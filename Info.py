#Ask user for name

name = input("What's your name: ")
#Ask user for age

age = input("What's your age: ")
#Ask user for city

city = input("What's your city: ")
#Ask user what the enjoy

enjoy = input("What do you enjoy: ")
#Create output text
string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name, age, city, enjoy)
#print output to screen
print(output)