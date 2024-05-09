class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()

    def describe_restaurant(self):
        print("Name:", self.restaurant_name)
        print("Type:", self.cuisine_type)

    def open_restaurant(self):
        print("Restaurant Is Open")
