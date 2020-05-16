from Models.Node import Node
from Models.PriorityQueue import PriorityQueue


class Huffman:

    nrSymbols = 4

    def get_encoding_dictionary(self, text):

        if text is None or len(text) is 0:
            return None

        dictionary = self.process(text)

        heap = self.build_heap(dictionary)
        s = (len(list(dictionary.values())) - self.nrSymbols) % (self.nrSymbols - 1) + 1
        r = self.nrSymbols

        huffman_tree = self.build_huffman_tree(heap, s, r)

        encoding_dictionary = {}

        self.build_encoding_dictionary(huffman_tree, encoding_dictionary, '')

        return encoding_dictionary

    def process(self, text):
        characters = []
        for char in text:
            characters.append(char)

        characters = list(set(characters))
        characters.sort()

        probabilities = []
        for char in characters:
            nr = text.count(char)
            probabilities.append(nr / len(text))

        return dict(zip(characters, probabilities))

    def build_heap(self, dictionary):

        characters = list(dictionary.keys())
        probabilities = list(dictionary.values())

        queue = PriorityQueue()
        for index in range(len(characters)):
            node = Node()
            node.set_character(characters[index])
            node.set_probability(probabilities[index])
            queue.insert(node)
        return queue

    def build_huffman_tree(self,heap, s, r):

        newProbability = 0
        newNode = Node()
        while s > 0:
            s = s - 1
            minimumNode = heap.extract_min()
            newProbability += minimumNode.get_probability()
            newNode.add_child(minimumNode)
            newNode.set_character(None)
            newNode.set_probability(newProbability)

        heap.insert(newNode)

        while True:
            rIndex = r
            newProbability = 0
            newNode = Node()
            while rIndex > 0:
                rIndex = rIndex - 1
                minimumNode = heap.extract_min()
                newProbability += minimumNode.get_probability()
                newNode.add_child(minimumNode)
                newNode.set_character(None)
                newNode.set_probability(newProbability)

            heap.insert(newNode)

            if heap.get_size() == 1:
                return heap.get_values()[0]

    def build_encoding_dictionary(self, root_node, coding_dictionary, currentCode):

        if root_node is None:
            return

        if root_node.is_leaf():
            coding_dictionary[root_node.get_character()] = currentCode
            return

        for index in range(len(root_node.get_children())):
            child = root_node.get_children()[index]
            self.build_encoding_dictionary(child, coding_dictionary, f'{currentCode}{index}')
