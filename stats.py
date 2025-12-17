def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = len(file_contents.split())
    print(f"Found {word_count} total words")

def character_count():
     with open("books/frankenstein.txt") as text:
        # Gets the text of the book counts them and ties them to dictonary pairs, while also lowercasing them all.
        character_count_dict = {}
        for character in text:
            if character.lower() not in character_count_dict:
                character_count_dict[character.lower()] = 1
            else:
                character_count_dict[character.lower()] += 1
        print(character_count_dict)

def main():
    get_book_text()
    character_count()


main()
