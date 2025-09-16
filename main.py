import sys
from stats import count_words, count_chars, sorted_list

def get_book_text(file):
    with open(file) as f:
      book_text =  f.read()
      return book_text
   

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file = sys.argv[1]
    contents = get_book_text(file)
    characters = count_chars(contents)
    is_sorted = sorted_list(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(contents)} total words")
    print("--------- Character Count -------")
    for character in is_sorted:
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")

        
   

main()

