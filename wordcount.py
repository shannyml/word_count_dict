"""Count words in file."""
read_file = open("twain.txt")

def make_word_counts_dict(read_file):
    word_counts = {}
    for line in read_file:
        line = line.rstrip()
        words = line.split(" ")
    
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
    
    for word, count in word_counts.items():
        print(word, count)

(make_word_counts_dict(read_file))