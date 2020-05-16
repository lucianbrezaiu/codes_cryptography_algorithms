from CodeWord import CodeWord


class CodeGenerator:

    length = 0
    distance = 0
    code_words = None
    word_generator = None

    def __init__(self, length, distance):
        self.length = length
        self.distance = distance
        self.code_words = []
        self.word_generator = iter(self.word_generation())

    def word_generation(self):
        for number in range(pow(2, self.length)):
            binary_format = "{:0{}b}"
            binary_representation = binary_format.format(number, self.length)
            yield CodeWord(binary_representation)

    def generate_word(self):
        return next(self.word_generator)

    def generate_code(self):
        first_word = self.generate_word()
        self.code_words.append(first_word)

        while True:
            try:
                possible_word = self.generate_word()
                if self.valid_word(possible_word):
                    self.code_words.append(possible_word)
            except Exception:
                break

        return self.code_words

    def valid_word(self, possible_word):
        for current_word in self.code_words:
            if CodeWord.get_distance(current_word, possible_word) < self.distance:
                return False
        return True

