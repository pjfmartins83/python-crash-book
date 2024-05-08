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


class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = Privileges(privileges) 

    def show_privileges(self):
        self.privileges.show_privileges()


class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


privilege_list = ["can add post", "can delete post", "can ban user"]
admin = Admin("Paulo", "Zé", privilege_list)
admin.show_privileges()
