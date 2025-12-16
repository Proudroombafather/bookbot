def get_book_text():
        with open("books/frankenstein.txt") as f:
                file_contents = f.read()
        word_count = len(file_contents.split())
        print(f"Found {word_count} total words")

def main():
        get_book_text()

main()
