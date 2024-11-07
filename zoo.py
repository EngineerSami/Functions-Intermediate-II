class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 100
        self.happiness = 100

    def display_info(self):
        print(f"Name: {self.name}, Health: {self.health}, Happiness: {self.happiness}")

    def feed(self):
        self.health += 10
        self.happiness += 10

class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.roar_level = 5

    def feed(self):
        super().feed()
        self.happiness += 5

class Tiger(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.stripe_pattern = "distinctive"

class Monkey(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.energy_level = 7

    def feed(self):
        super().feed()
        self.health += 5

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, animal):
        self.animals.append(animal)

    def print_all_info(self):
        print("-" * 30, "Sami's Zoo", "-" * 30)
        for animal in self.animals:
            animal.display_info()

zoo1 = Zoo("John's Zoo")
zoo1.add_animal(Lion("Nala", 3))
zoo1.add_animal(Lion("Simba", 4))
zoo1.add_animal(Tiger("Rajah", 5))
zoo1.add_animal(Tiger("Shere Khan", 6))
zoo1.add_animal(Monkey("George", 2))
zoo1.print_all_info()

for animal in zoo1.animals:
    animal.feed()


print("\nAfter feeding the animals:\n")
zoo1.print_all_info()

