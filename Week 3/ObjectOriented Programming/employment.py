# Classs definition for employees and derived classes.
class Employees:
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last

class Supervisors(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password

class Chefs(Employees):
    def leave_request(self, days):
        return f"May I take a leave for {days} days"

# Instantiation of objects.
adrian = Supervisors("Adrian", "A", "applepie")
emily = Chefs("Emily", "E")
juno = Chefs("Juno", "J")

# issubclass isinstance
if issubclass(Chefs, Employees):
    print('Chefs are employees.')
if isinstance(emily, Chefs):
    print("Emily is a chef.")