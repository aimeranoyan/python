class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"It's {self.title}'s draw time, buddy"


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"You took a {self.title}. {self.title}'s draw time"


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"You took a {self.title}. {self.title}'s draw time"


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"You took a {self.title}. {self.title}'s draw time"


pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')

print(pen.draw())
print(pencil.draw())
print(handle.draw())