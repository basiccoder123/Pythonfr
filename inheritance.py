class FamilyMember:
    def __init__(self, eye_colour, height_cm):
        self.eye_colour = eye_colour
        self.height_cm = height_cm
    def show_traits(self):
        print("Eye Colour:", self.eye_colour)
        print("Height(cm):", self.height_cm)

class kid(FamilyMember):
    def __init__(self, name, age, eye_colour, height_cm):
        self.name = name
        self.age = age
        super().__init__(eye_colour, height_cm)

    def show_traits(self):
        print("Name:", self.name)
        print("Age:", self.age)
        super().show_traits()

    def favorite_hobby(self, hobby):
        print(self.name, "loves", hobby)

child = kid("Kirk", 14, "brown", 185)

child.show_traits()
child.favorite_hobby("football")

print("Is kid a subclass of FamilyMember?", issubclass(kid, FamilyMember))