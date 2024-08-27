class Car:
    # Blueprint
    def __init__(self,brand,name): #constructor
        #data members
        self.name = name
        self.wheels = 4
        self.brand = brand

    def show_car(self):
        # member functions
        print("I am driving a ", self.brand, " model: ",self.name)

# creating objects
bmw = Car("BMW", "X3")
audi = Car("Audi","Q7")
merc = Car("Mercedes", "S-class") #keep on creating objects & reuse the class code

bmw.show_car()
merc.show_car()
audi.show_car()

