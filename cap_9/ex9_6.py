class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()

    def describe_restaurant(self):
        print("Name:", self.restaurant_name)
        print("Type:", self.cuisine_type)


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours

    def describe_flavours(self):
        for flavour in self.flavours:
            print(flavour.title())


icecream = IceCreamStand("Sorveteria Teste", "sorveteria", "chocolate")
icecream.flavours = ["chocolate", "morango", "baunilha"]
icecream.describe_restaurant()
icecream.describe_flavours()
