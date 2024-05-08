class User():
    def __init__(self, first_name, last_name, email, passwoord, age, country):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email
        self.password = passwoord
        self.age = age
        self.country = country.title()
        self.login_attempts = 0

    def describe_user(self):
        print("Name:", self.first_name, self.last_name)

    def greet_user(self):
        print("Hello, " + self.first_name.title() + " " + self.last_name.title() + ". Welcome to our site!")

    def increment_login_attempts(self, increment):
        new_value = self.login_attempts + increment
        old_value = self.login_attempts
        self.login_attempts = new_value if increment > 0 else old_value

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User("paulo", "martins", "pjfmartins83@gmail.com", "123456", "40", "brasil")
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts(5)
print(user1.increment_login_attempts)
user1.reset_login_attempts
print(user1.reset_login_attempts)
