class Recipe():
    print("Recipe class defined.")

    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print(f"The {self.dish} has {self.items} and takes {self.time} min to prepare.")

pizza = Recipe("Pizza", ["cheese", "bread", "tomato"], 45)
burger = Recipe("Burger", ["bread", "meat", "tomato"], 35)
pizza.contents()