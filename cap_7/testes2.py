print("Task 7.4")

prompt = '\nGive me a toppings Your pizza'
prompt += "\n(If you stop a giving a topping, write a 'end'"

while True:
    topping = input(prompt)
    if topping != 'end':
        print(f"  I add {topping} to your pizza.")
    else:
        break
