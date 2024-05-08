class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = number_served

    def describe_restaurant(self):
        print("Name:", self.restaurant_name)
        print("Type:", self.cuisine_type)

    def open_restaurant(self):
        print("Restaurant Is Open")

    def set_number_served(self, served):
        self.number_served = served

    def new_sale(self):
        self.number_served += 1


restaurant1 = Restaurant("la Lolla", "À La Carte")
restaurant2 = Restaurant("Cheiro Verde", "Por kg")
restaurant3 = Restaurant("Mirante", "Frutos do Mar")
restaurant4 = Restaurant("Teste", "rodízio", "5")
restaurant4.set_number_served(10)
restaurant4.new_sale()
print(restaurant4.number_served)
