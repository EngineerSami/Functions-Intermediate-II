class Country:
    def __init__(self, name):
        self.name = name

class India(Country):
    def __init__(self):
        super().__init__("India")
    
    def print_continent(self):
        print("Asia")

class France(Country):
    def __init__(self):
        super().__init__("France")
    
    def print_continent(self):
        print("Europe")


obj1 = India()
obj1.print_continent()

obj2 = France()
obj2.print_continent()
