class User():
    def __init__(self, first_name, last_name, email, passwoord, age, country):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email
        self.password = passwoord
        self.age = age
        self.country = country.title()

    def describe_user(self):
        print("Name:", self.first_name, self.last_name)

    def greet_user(self):
        print("Hello, " + self.first_name.title() + " " + self.last_name.title() + ". Welcome to our site!")


user1 = User("paulo", "martins", "pjfmartins83@gmail.com", "123456", "40", "brasil")
user1.describe_user()
user1.greet_user()
