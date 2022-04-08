class Banana:
    """A tasty tropical fruit"""
    def peel(self):
        self.peeled = True

    def set_color(self, color):
        """Set the color of the banana"""
        if color in self.colors:
            self.color = color
        else:
            raise ValueError(f'A banana cannot be {color}!')

my_banana = Banana()
my_banana.set_color('green')
my_banana.peel()

print(my_banana)