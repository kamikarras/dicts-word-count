# put your code here.
# open file
# iterate through each line
# split each line into list by whitespace
# iterate through list
# declare a dictionary
# add items to count
# return dictionary


def word_counter(filename):
    """
    Takes a file and returns a dictionary of all the words and their counts

    """

    word_counts = {}
    all_words = []

    with open(filename, "r") as f:
        for line in f:
            line = line.rstrip()
            all_words.extend(line.split())

    for word in all_words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def print_word_counts(word_counts):
    """
    Takes dictionary and prints out each word and its count
    """

    for word, count in word_counts.items():
        print(f'{word} {count}')


counts = word_counter("twain.txt")
print_word_counts(counts)
