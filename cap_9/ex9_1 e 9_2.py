class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()

    def describe_restaurant(self):
        print("Name:", self.restaurant_name)
        print("Type:", self.cuisine_type)

    def open_restaurant(self):
        print("Restaurant Is Open")


restaurant1 = Restaurant("la Lolla", "À La Carte")
restaurant2 = Restaurant("Cheiro Verde", "Por kg")
restaurant3 = Restaurant("Mirante", "Frutos do Mar")

restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant2.describe_restaurant()
restaurant2.open_restaurant()
restaurant3.describe_restaurant()
restaurant3.open_restaurant()
