def show_ingredients(*ingredients):
    print("Esses são os ingredientes que você escolheu:")
    for ing in ingredients:
        print(ing.title())


show_ingredients("frango")
show_ingredients("frango", "maionese")
show_ingredients("presunto", "tomate", "alface")
