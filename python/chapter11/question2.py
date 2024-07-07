# create a class 'pets' from a class 'animals' and further createa a class 'dog' from 'pets' add a method 'bark' to class dog
class animal:
    pass
class pets(animal):
    pass
class dog(pets):
    @staticmethod
    def bark():
        print("Bow Bow")

dog.bark()