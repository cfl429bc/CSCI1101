import sys

def get_word_counts():
    word_counts = {}
    print("Enter words, each on their own line, Ctrl-D to stop:")
    try:
        while True:
            line = input().strip().lower()
            if line:
                words = line.split()
                for word in words:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1
    except EOFError:
        pass

    return word_counts

def find_max_count(dict):
    

words = get_word_counts()
print(words)