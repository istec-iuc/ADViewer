class GraphNode():
    def __init__(self, posx, posy, name, size=10, color="b"):
        self.x = posx
        self.y = posy
        self.name = name
        self.size = size
        self.color = color

    def __str__(self):
        return f"(x: {self.x}, y: {self.y}, name: {self.name}, size: {self.size}"


