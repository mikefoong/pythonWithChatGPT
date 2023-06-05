strings = input("Enter your name and age separated by a space: ")
data = {}
name, age = strings.split()
data[name] = age
print(data)

