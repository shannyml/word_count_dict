"""Count words in file."""

import sys

read_file = open(sys.argv[1])  #sys.argv helps with giving user the option to open any files


def tokenize(read_file):
    words_in_file = []
    for line in read_file:
        line = line.rstrip()
        words = line.split(" ")
        for word in words: 
            words_in_file.extend(word)
        # words_in_file = [word for word in words]
    #     print(words_in_file)
    # return words_in_file
        print(words)
    return words    

def count_words(read_file):
    words_in_file = tokenize(read_file)
    words_count = {}
    for word in words_in_file:
        words_count[word] = words_count.get(word, 0) + 1
    return words_count

def print_word_counts(read_file):
    words_count = count_words(read_file)
    for word, count in words_count.items():
        print(word, count)

print_word_counts(read_file)