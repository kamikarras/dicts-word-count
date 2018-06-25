# put your code here.
# open file
# iterate through each line
# split each line into list by whitespace
# iterate through list
# declare a dictionary
# add items to count
# return dictionary
import sys
from collections import Counter


def word_counter(filename):
    """
    Takes a file and returns a dictionary of all the words and their counts

    """

    with open(filename) as f:
        read_data = f.read()
        word_list = [word.strip(".,-/?!").lower()
                     for word in read_data.split()]

        word_counts = Counter(word_list)

    return word_counts


def print_word_counts(word_counts):
    """
    Takes dictionary and prints out each word and its count
    """

    for word, count in word_counts.items():
        print(f'{word} {count}')


counts = word_counter(sys.argv[1])
print_word_counts(counts)
