def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    print(count_words(text))
    print(letter_count(text))


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def letter_count(text):
    count = {}
    lowercase = text.lower()

    for word in lowercase:
        for letter in word:
            if letter not in count:
                count[letter] = 1
            else:
                count[letter] += 1
    return count

main()