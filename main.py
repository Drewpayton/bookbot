def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    print("-- Begin report of books/frankenstein.txt --")
    print(f"{count_words(text)} words were found in the document\n")
    letter_count(text)
    print("-- End Report --")
    



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

    return sort_on(count)

def sort_on(text):
    text = sorted(text.items(), reverse=True, key=lambda x:x[1])

    for key, value in text:
        if str(key).isalpha():
            print(f"The '{key}' character was found {value} times")

main()