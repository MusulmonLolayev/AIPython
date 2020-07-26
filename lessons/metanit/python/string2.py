#! program which counts number of words in text file
import os


def get_words(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").\
        replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words


def get_words_dict(words):
    words_dict = dict()

    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict


def main():
    filename = input("Enter the location of file in computer: ")
    if not os.path.exists(filename):
        print("The file doesn't exist")
    else:
        words = get_words(filename)
        words_dict = get_words_dict(words)
        print("Number of words: %d" % len(words))
        print("Number of unique words: %d" % len(words_dict))
        print("All words in text:")
        for word in words_dict:
            print(word.ljust(20), words_dict[word])


if __name__ == "__main__":
    main()