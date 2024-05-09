from modulo_user import User
from modulo_admin_privileges import Privileges


class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = Privileges(privileges)

    def show_privileges(self):
        self.privileges.show_privileges()

privilege_list = ["can add post", "can delete post", "can ban user"]
admin = Admin("Paulo", "Martins", privilege_list)
admin.show_privileges()
