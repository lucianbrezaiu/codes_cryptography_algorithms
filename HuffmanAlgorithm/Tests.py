import unittest
from Models.Node import Node
from Helper import Helper
from Huffman import Huffman
from Models.PriorityQueue import PriorityQueue


class Tests(unittest.TestCase):

    def test_queue_insert(self):
        queue = PriorityQueue()
        self.assertEqual(queue.is_empty(), True)
        queue.insert(8)
        self.assertEqual(queue.is_empty(), False)

    def test_queue_get_min(self):
        queue = PriorityQueue()
        queue.insert(8)
        queue.insert(6)
        self.assertEqual(queue.get_min(), 6)

    def test_queue_extract_min(self):
        queue = PriorityQueue()
        queue.insert(8)
        queue.insert(6)
        queue.insert(4)
        minValue = queue.extract_min()
        self.assertEqual(minValue, 4)
        self.assertEqual(queue.get_min(), 6)

    def test_queue_get_size(self):
        queue = PriorityQueue()
        queue.insert(8)
        queue.insert(6)
        queue.insert(4)
        self.assertEqual(queue.get_size(), 3)

    def test_node(self):
        node1 = Node()
        node1.set_character('a')
        node1.set_probability('1')
        self.assertEqual(node1.get_character(), 'a')
        self.assertEqual(node1.get_probability(), '1')
        self.assertTrue(node1.is_leaf())

    def test_node_get_character(self):
        node = Node()
        node.set_character('a')
        self.assertEqual(node.get_character(), 'a')

    def test_node_get_probability(self):
        node = Node()
        node.set_probability('1')
        self.assertEqual(node.get_probability(), '1')

    def test_node_comparison(self):
        node1 = Node()
        node1.set_probability('1')
        node2 = Node()
        node2.set_probability('2')
        self.assertTrue(node1 < node2)

    def test_node_add_child(self):
        node = Node()
        self.assertTrue(node.is_leaf())
        node.add_child(Node())
        self.assertFalse(node.is_leaf())

    def test_huffman(self):
        text = Helper.read_file("input.txt")
        huffman = Huffman()
        encoding_dictionary = huffman.get_encoding_dictionary(text)
        encoded_text = Helper.encoding(encoding_dictionary, text)
        decoded_text = Helper.decoding(encoding_dictionary, encoded_text)
        self.assertEqual(text, decoded_text)


if __name__ == '__main__':
    unittest.main()


