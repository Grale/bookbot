def get_num_words(path_to_file):
    with open(path_to_file, 'r') as f:
        file_contents = f.read()
    book_words = file_contents.split()
    return len(book_words)


def get_num_characters(path_to_file):
    book_chars = {}
    with open(path_to_file, 'r', encoding="utf-8") as f:
        file_contents = f.read()
    l_file_contents = file_contents.lower()
    for character in l_file_contents:
        if character not in book_chars:
            book_chars[character] = 1
        else:
            book_chars[character] += 1
    return book_chars


def sort_on(items):
    return items["num"]

def sorted_list(book_chars):

    new_list = []
    for character in book_chars:
        new_dic = {}
        new_dic["char"] = character
        new_dic["num"] = book_chars[character]
        new_list.append(new_dic)
    new_list.sort(reverse=True, key=sort_on)
    return new_list





    print(new_dic)
