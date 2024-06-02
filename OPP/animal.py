class Animal:
    def  make_sound(self):
        pass
    def move(self):
        pass

    def talk(self):
        pass
class Bird:
    def make_sound(self):
        print("Chirp")

    def move(self):
        print("The bird is fying")

    def reproduce(self):
        print("A bird can lay eggs")


class Fish(Animal):
    def make_sound(self):
        print("Click")

    def move(self):
        print("swimming")

    def reproduce(self):
        print("The fish lays eggs")

class Dog(Animal):
    def make_sound(self):
        print("Baking")

    def move(self):
        print("The dog is running")

    def reproduce(self):
        print("Give birth")

class Cow(Animal):
    def make_sound(self):
        print("Moos")

    def move(self):
        print("The cow is walking")

    def reproduce(self):
        print("A cow gives birth")
