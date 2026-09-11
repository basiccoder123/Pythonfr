class myClass:
    __privateVar = 27

    def __privMeth(self):
        print("Im inside a class")

    def hello(self):
        print("Value of private variable:",myClass.__privateVar)


foo = myClass()

foo.hello()
foo.__privMeth()
