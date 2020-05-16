import time
import Tests
import unittest
from Helper import Helper
from Huffman import Huffman


def run_tests():
    print()
    time.sleep(0.5)
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromModule(Tests))


def __main__():

    text = Helper.read_file("input.txt")
    encoding_dictionary = Huffman().get_encoding_dictionary(text)

    encoded_text = Helper.encoding(encoding_dictionary, text)
    decoded_text = Helper.decoding(encoding_dictionary, encoded_text)

    print(f"\nEncoded text: {encoded_text}")
    print(f"\nDecoded text: {decoded_text}")

    run_tests()


__main__()
