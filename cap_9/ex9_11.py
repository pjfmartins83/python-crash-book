from modulo_user_complete import Admin

privilege_list = ["can add post", "can delete post", "can ban user"]
admin = Admin("Paulo", "Martins", privilege_list)
admin.show_privileges()
