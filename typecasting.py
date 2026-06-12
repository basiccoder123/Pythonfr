name = "Cow"
age = 2
weight = 40.5
is_student = False

#before typecasting
print("Name is", name)
print("Data type is:", type(name))

print("Age is", age)
print("Data type is:", type(age))

print("Weight is:", weight)
print("Data type is:", type(weight))

print("Is",name,"a student", is_student)
print("Data type is:", type(is_student))

#after typecasting
weight = int(weight)
print("New data type is:", type(weight))

age = str(age)
print("New data type is:", type(age))
