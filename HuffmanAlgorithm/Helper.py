class Helper:

    @staticmethod
    def read_file(filename):
        file = open(filename, "r")
        text = file.read()
        return text

    @staticmethod
    def encoding(encoding_dictionary, input):
        encodedText = ''
        for char in input:
            encodedText += encoding_dictionary[char]
        return encodedText

    @staticmethod
    def decoding(encoding_dictionary, input):

        decodedText = ''
        possibleCode = ''
        for char in input:
            possibleCode += char
            if possibleCode in encoding_dictionary.values():
                keysList = list(encoding_dictionary.keys())
                valuesList = list(encoding_dictionary.values())

                decodedLetter = keysList[valuesList.index(possibleCode)]
                decodedText += decodedLetter
                possibleCode = ''
        return decodedText
