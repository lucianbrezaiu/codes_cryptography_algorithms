from CodeGenerator import CodeGenerator
import time
import Tests
import unittest


def run_tests():
    print()
    time.sleep(0.5)
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromModule(Tests))


def read_inputs():
    try:
        n = int(input("Insert length: "))
        d = int(input("Insert distance: "))
        return n, d
    except Exception:
        print("\nError occurred!\n")
        return read_inputs()


def __main__():
    length, distance = read_inputs()

    code_generator = CodeGenerator(length, distance)

    code_words = code_generator.generate_code()

    if len(code_words) == 1:
        print("No code!")
    else:
        print(f"{len(code_words)} words:")
        for word in code_words:
            print(word)

    run_tests()


__main__()
