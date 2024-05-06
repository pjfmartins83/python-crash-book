class Restaurant():
    self.restaurant_name = restaurant_name.title()
    self.cuisine_type = cuisine_type.title()

def describe_restaurant(self):
    print("Name: ", self.restaurant_name)
    print("Type: ", self.cuisine_type)

def open_restaurant(self):
    self.open = True
    print("Restaurant is now open!")

res1 = Restaurant("Happy Lotus","Chinese")
res2 = Restaurant("Dancing Sombrero","Mexican")
res3 = Restaurant("Feisty Pretzel","German")

res1.describe_restaurant()
res2.describe_restaurant()
res3.describe_restaurant()
