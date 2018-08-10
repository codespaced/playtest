class Menu:
    def __init__(self, name: str, options: dict=None):
        self.name = name
        if options is None:
            self.options = {}
        else:
            self.options = options

    def display(self):
        for choice, option in self.options.items():
            print(f"({choice}).  {option}")
