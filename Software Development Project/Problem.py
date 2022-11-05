class Problem:
    def __init__(self, problem):
        self.problem = problem

    def problem_info(self):
        return self.problem

    # records the problem, if the user inputs password change, gives the change password function.
    # getting the first 2 characters of Staff ID and First name
    def password_change(self):
        if "password" or "change" in self.problem:
            print("Let's change your password")