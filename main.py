from stats import get_num_characters, get_num_words,sorted_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book = get_num_characters(sys.argv[1])

#print(book)



print("============ BOOKBOT ============")
print(f"Analyzing book found at books/frankenstein.txt...")
print(f"----------- Word Count ----------")
print(f"Found {get_num_words('books/frankenstein.txt')} total words")
print(f"--------- Character Count -------")
get_list = sorted_list(book)

for element in get_list:
    if  element["char"].isalpha():
        print(f"{element["char"]}: {element["num"]}")


print(f"============= END ===============")