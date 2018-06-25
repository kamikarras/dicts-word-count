# put your code here.
# open file
# iterate through each line
# split each line into list by whitespace
# iterate through list
# declare a dictionary
# add items to count
# return dictionary
import sys


def word_counter(filename):
    """
    Takes a file and returns a dictionary of all the words and their counts

    """

    word_counts = {}

    with open(filename) as f:
        for line in f:
            for word in line.split():
                word = word.strip(".,-/?!").lower()
                word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def print_word_counts(word_counts):
    """
    Takes dictionary and prints out each word and its count
    """

    for word, count in word_counts.items():
        print(f'{word} {count}')


counts = word_counter(sys.argv[1])
print_word_counts(counts)
