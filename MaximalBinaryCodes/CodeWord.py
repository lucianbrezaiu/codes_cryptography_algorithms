class CodeWord:

    bits_list = []

    def __init__(self, binary_representation):
        self.bits_list = []
        for bit in binary_representation:
            self.bits_list.append(bit)

    def get_length(self):
        return len(self.bits_list)

    def get_bits(self):
        return self.bits_list

    def __str__(self):
        return "".join(self.bits_list)

    @staticmethod
    def get_distance(word1, word2):

        if word1.get_length() != word2.get_length():
            raise Exception("Words don't have same length!")

        first_list = word1.get_bits()
        second_list = word2.get_bits()

        distance = sum(1 for a, b in zip(first_list, second_list) if a != b)

        return distance
