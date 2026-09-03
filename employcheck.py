class Employee:
    def __init__(self):
        print("Employee Created")

    def __del__(self):
        print("Destruction Called...")

def create_obj():
    print("Making Object...")
    obj = Employee()
    print("Function End...")
    return obj

print("Calling create_obj() funtion")

obj = create_obj()

print("Program End...")

