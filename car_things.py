class Vehicle:
    def __init__(self, name, worth, model) -> None:
        self.name = name
        self.worth = worth
        self.model = model
        print(f'''
              Name: {self.name}, 
              Worth: #{self.worth}, 
              Model: {self.model}''')
        





if __name__ == '__main__':
    car1 = Vehicle('Red Convertible', 600000, 'Benz')
    car2 = Vehicle('Blue Van', 1000000, 'Toyota')