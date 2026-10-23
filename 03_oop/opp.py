class Car:
    def __init__(self, brand, name, owner):
        self.brand = brand
        self.name = name
        self.__owner = owner

    def car_info(self):
        print(f"Car brand is: {self.brand} & name is: {self.name}")

    def get_owner(self):
        return self.__owner
    

car1 = Car("Tata", "Nexon", "Rahul")

car1.car_info()
print(car1.get_owner())

#############################

class Tata(Car):
    def __init__(self, brand, name, owner, dealar):
        super().__init__(brand, name, owner)
        self.dealar = dealar

    def delar_info(self):
        print(f"Dealar is: {self.dealar} and Owner is {self.get_owner()}")

tata_car_1 = Tata("Tata", "Punch", "Niraj", "ADTP")

tata_car_1.delar_info()

###################################
