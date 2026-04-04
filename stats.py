def num_words_in_text(text):
    list_text = text.split()
    print(f"Found {len(list_text)} total words")

def count_characters(text):
    char_counts = {}

    for char in text:
        char = char.lower()  # normalize

        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts
