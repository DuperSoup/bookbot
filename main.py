def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)

def word_count():
    book_text = get_book_text("books/frankenstein.txt")
    text = book_text.split()
    word_count = len(text)
    # print(word_count)
    return word_count

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def character_count():
    # initialize characters dictionary
    characters_dict = {}
    
    book_text = get_book_text("books/frankenstein.txt").lower()
    book_text_characters = list(book_text)

    for char in book_text_characters:
        if char in characters_dict:
            characters_dict[char] += 1            
        else:
            characters_dict[char] = 1    

    # print(characters_dict)
    return characters_dict

def convert_to_list_of_dicts(dict):
    list_of_dicts = []
    for letter, count in dict.items():
        if letter.isalpha():    
            list_of_dicts.append({'char': letter, 'count': count})
    

    # print(list_of_dicts)
    return list_of_dicts
    
def sort_on(dict):
    return dict['count']

def sort_list_of_dicts(dict):
    dict.sort(reverse=True, key=sort_on)
    # print(dict)     
    return dict

def print_report(word_count, sorted_list_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for dict in sorted_list_dict:
        letter = dict["char"]
        count = dict["count"]
        print(f"The {letter} character was found {count} times")
    print(" --- End report ---")

            

# main()

word_count = word_count()
characters_count = character_count()
list_of_char_dicts = convert_to_list_of_dicts(characters_count)
sorted_list_of_char_dicts = sort_list_of_dicts(list_of_char_dicts)
print_report(word_count, sorted_list_of_char_dicts)
