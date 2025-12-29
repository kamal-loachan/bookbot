from stats import num_words_in_text

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    print(get_book_text("books/frankenstein.txt"))

num_words_in_text(get_book_text("books/frankenstein.txt"))