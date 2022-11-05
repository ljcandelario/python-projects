class User:

    def __init__(self, staff_id, name, email):
        self.staff_id = staff_id
        self.name = name
        self.email = email

    def user_info(self):
        return self.staff_id, self.name, self.email