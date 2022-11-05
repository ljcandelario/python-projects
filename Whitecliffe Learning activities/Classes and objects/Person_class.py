class Person:

    def __init__(self, age, gender, address, height):
        self.age = age
        self.gender = gender
        self.address = address
        self.height = height

    def myIntro(self):
        print('Hello my age is', self.age)  # , is used when we need to show int or float values.
        print("Hello my gender is " + self.gender)
        print('My address is ', self.address)
        print('My height is ', self.height)



harry = Person(36, "male", "123 Nice Street", "170cm")
print(harry.myIntro())
