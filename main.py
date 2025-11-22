from stats import get_num_words, get_char_count, sorted_char_count
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    args = sys.argv
    if not len(args) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = args[1]
    print("============ BOOKBOT ============")
    text = get_book_text(book)
    print(f"Analyzing book found at {book}...")
    num_words = get_num_words(text=text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    num_chars = get_char_count(text=text)
    sorted = sorted_char_count(num_chars)
    print("--------- Character Count -------")
    for item in sorted:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["nums"]}")
    
    print("============= END ===============")
    
    
    
main()