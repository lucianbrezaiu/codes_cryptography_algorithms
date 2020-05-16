import unittest
from CodeGenerator import CodeGenerator
from CodeWord import CodeWord


class Tests(unittest.TestCase):

    def test_code_1(self):
        code_length = 5
        code_distance = 3

        code_generator = CodeGenerator(code_length, code_distance)
        code_words = code_generator.generate_code()

        for word in code_words:
            self.assertEqual(word.get_length(), code_length)

        for i in range(0, len(code_words)):
            for j in range(i + 1, len(code_words)):
                word_distance = CodeWord.get_distance(code_words[i], code_words[j])
                self.assertEqual(word_distance >= code_distance, True)

    def test_code_2(self):
        code_length = 7
        code_distance = 3

        code_generator = CodeGenerator(code_length, code_distance)
        code_words = code_generator.generate_code()

        for word in code_words:
            self.assertEqual(word.get_length(), code_length)

        for i in range(0, len(code_words)):
            for j in range(i + 1, len(code_words)):
                word_distance = CodeWord.get_distance(code_words[i], code_words[j])
                self.assertEqual(word_distance >= code_distance, True)

    def test_code_3(self):
        code_length = 9
        code_distance = 3

        code_generator = CodeGenerator(code_length, code_distance)
        code_words = code_generator.generate_code()

        for word in code_words:
            self.assertEqual(word.get_length(), code_length)

        for i in range(0, len(code_words)):
            for j in range(i + 1, len(code_words)):
                word_distance = CodeWord.get_distance(code_words[i], code_words[j])
                self.assertEqual(word_distance >= code_distance, True)

    def test_code_4(self):
        code_length = 10
        code_distance = 3

        code_generator = CodeGenerator(code_length, code_distance)
        code_words = code_generator.generate_code()

        for word in code_words:
            self.assertEqual(word.get_length(), code_length)

        for i in range(0, len(code_words)):
            for j in range(i + 1, len(code_words)):
                word_distance = CodeWord.get_distance(code_words[i], code_words[j])
                self.assertEqual(word_distance >= code_distance, True)

    def test_code_4(self):
        code_length = 10
        code_distance = 5

        code_generator = CodeGenerator(code_length, code_distance)
        code_words = code_generator.generate_code()

        for word in code_words:
            self.assertEqual(word.get_length(), code_length)

        for i in range(0, len(code_words)):
            for j in range(i + 1, len(code_words)):
                word_distance = CodeWord.get_distance(code_words[i], code_words[j])
                self.assertEqual(word_distance >= code_distance, True)
