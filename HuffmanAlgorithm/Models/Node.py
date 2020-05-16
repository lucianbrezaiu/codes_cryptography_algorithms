class Node:

    char = ''
    probability = 0
    children = []

    def __init__(self):
        self.char = ''
        self.probability = 0
        self.children = []

    def __str__(self):
        return f"({self.char},{self.probability})"

    def __lt__(self, other):
        if other is None:
            return -1
        if not isinstance(other, Node):
            return -1
        return self.probability < other.probability

    def add_child(self, value):
        self.children.append(value)

    def get_probability(self):
        return self.probability

    def set_probability(self, probability):
        self.probability = probability

    def get_character(self):
        return self.char

    def set_character(self, char):
        self.char = char

    def get_children(self):
        return self.children

    def is_leaf(self):
        return len(self.children) == 0
