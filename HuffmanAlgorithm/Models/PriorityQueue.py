class PriorityQueue:

    def __init__(self):
        self.values = []

    def __str__(self):
        str = ""
        for value in self.values:
            str += f"{value} "
        str += "\n"
        return str

    def insert(self, value):
        self.values.append(value)
        self.sift_up(len(self.values) - 1)

    def sift_down(self, position):
        son = position
        if 2*position+1 < len(self.values) and self.values[son] > self.values[2 * position + 1]:
            son = 2 * position + 1
        if 2*position+2 < len(self.values) and self.values[son] > self.values[2 * position + 2]:
            son = 2 * position + 2

        if position != son:
            aux = self.values[position]
            self.values[position] = self.values[son]
            self.values[son] = aux
            self.sift_down(son)

    def sift_up(self, position):
        middle = (position - 1) // 2
        while middle >= 0 and self.values[middle] > self.values[position]:
            aux = self.values[position]
            self.values[position] = self.values[middle]
            self.values[middle] = aux
            position = middle
            middle = (position - 1) // 2

    def extract_min(self):
        minimum = self.values[0]
        self.values[0] = self.values[len(self.values) - 1]
        self.values[len(self.values) - 1] = minimum
        self.values.pop(len(self.values) - 1)
        self.sift_down(0)
        return minimum

    def get_min(self):
        return self.values[0]

    def is_empty(self):
        return len(self.values) == 0

    def get_size(self):
        return len(self.values)

    def get_values(self):
        return self.values
