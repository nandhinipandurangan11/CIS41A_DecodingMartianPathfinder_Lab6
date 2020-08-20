# CIS41A: Lab6: Nandhini Pandurangan
# This program imitates the ASCII table set up around the Pathfinder Martian
# lander in the movie the Martian
# Regular Expressions, comprehensions, maps, generators, and lambdas are used
# to convert the given data into ASCII characters


import re


class Martian:
    def __init__(self):
        """Constructor initializes a dictionary"""

        # Hexadecimal dictionary for letters A-F
        self.Hex_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    def read_file(self):
        """
        Reads the file HexDegrees, and parses the file through Regular Expressions.
        Data is of type string and is stored in a list.
        """

        file = open("HexDegrees.txt")
        degree_pairs_list = []

        # extracting the pairs of numbers
        for line in file:
            if line != "":
                target = line
                pattern = re.compile("\(\d+,\d+\)")
                degree_pairs_list = pattern.findall(target)
        file.close()

        return degree_pairs_list


    def str_to_int_generator(self, degree_pairs_list):
        """
        A generator that converts degrees in type string into
        degrees of type int through Regular Expressions
        """

        for pair in degree_pairs_list:
            target = pair
            pattern = re.compile("\d+\d+")  # the pattern we are looking for
            degree_pair = pattern.findall(target)
            degree_pair[0] = int(degree_pair[0])

            if len(degree_pair) > 1:
                degree_pair[1] = int(degree_pair[1])

            yield degree_pair

    def degree_to_hex_converter(self, degree):
        """
        Translates the integer degree into Hex based
        on the Hex Degree Range
        """

        if 0 <= degree < 22.5:
            hex = 0
        elif 22.5 <= degree < 45.0:
            hex = 1
        elif 45.0 <= degree < 67.5:
            hex = 2
        elif 67.5 <= degree < 90.0:
            hex = 3
        elif 90.0 <= degree < 112.5:
            hex = 4
        elif 112.5 <= degree < 135.0:
            hex = 5
        elif 135.0 <= degree < 157.5:
            hex = 6
        elif 157.5 <= degree < 180.0:
            hex = 7
        elif 180.0 <= degree < 202.5:
            hex = 8
        elif 202.5 <= degree < 225.0:
            hex = 9
        elif 225.0 <= degree < 247.5:
            hex = 'A'
        elif 247.5 <= degree < 270.0:
            hex = 'B'
        elif 270.0 <= degree < 292.5:
            hex = 'C'
        elif 292.5 <= degree < 315.0:
            hex = 'D'
        elif 315.0 <= degree < 337.5:
            hex = 'E'
        else:
            hex = 'F'

        return hex

    def make_hex_pair(self, degree_pair):
        """
        For each degree pair, it creates a hex pair by calling degree_to_hex_converter()
        """
        hex_pair = []
        degree_pair[0] = self.degree_to_hex_converter(degree_pair[0])
        hex_pair.append(degree_pair[0])
        if len(degree_pair) > 1:
            degree_pair[1] = self.degree_to_hex_converter(degree_pair[1])
            hex_pair.append(degree_pair[1])

        return hex_pair

    def convert_to_ascii(self, hex_list):
        """
        Given a list of hex pairs, converts each hex pair to one ascii value
        """
        ascii_list = []
        ascii_1 = 0
        ascii_2 = 0
        for hex_pair in hex_list:
            if type(hex_pair[0]) == int:
                ascii_1 = 16 * hex_pair[0]

            # Hex dictionary is used if the hex value is a letter
            else:
                ascii_1 = self.Hex_dict.get(hex_pair[0])

            if len(hex_pair) > 1:
                if type(hex_pair[1]) == int:
                    ascii_2 = 16 * hex_pair[1]
                else:
                    ascii_2 = self.Hex_dict.get(hex_pair[1])

            # ascii value is created by adding the hex pair together
            ascii_value = ascii_1 + ascii_2

            # list of ascii values are created
            ascii_list.append(ascii_value)

        return ascii_list

    def ascii_to_char(self, ascii_list):
        """ Uses map and lambda to convert ascii value into a character """

        return list(map(lambda num: chr(num), ascii_list))

    def print_chr_list(self, chr_list):
        """ Uses join to concatenate the character list"""

        separator = ""
        print(separator.join(chr_list))

    def main(self):
        # reads the file and parses it
        degree_pairs_list = self.read_file()

        # For each degree pair, converts it from str to int, and finds the hex value
        # Returns each hex pair as a list: [6, 'E'] and appends it to a hex_list
        # a comprehension is used to accomplish this
        hex_list = []
        [hex_list.append(self.make_hex_pair(int_pair)) for int_pair in self.str_to_int_generator(degree_pairs_list)]

        # Convert each hex pair into ascii code
        ascii_list = self.convert_to_ascii(hex_list)

        # convert the ascii value into character
        chr_list = self.ascii_to_char(ascii_list)

        # concatenate the character list into a "readable" sentence
        self.print_chr_list(chr_list)


# creating a Martian Object and calling the Martian method main()
m = Martian()
m.main()
