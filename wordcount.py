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

    