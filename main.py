def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_text = f.read()
    return book_text

def main():
    print(get_book_text("books/frankenstein.txt"))

main()