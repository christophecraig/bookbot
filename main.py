with open('./books/frankenstein.txt') as f:
    file_contents = f.read()

# Region utils

# A function that takes a string and returns a list of the characters in the string
def char_range(start, end):
    for character in range(ord(start), ord(end)):
        yield chr(character)

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["occurences"]

# Endregion utils

def count_words(book): 
    return len(book.split())

def count_every_letter(book):
    book = book.lower()
    the_dictionnary = []
    for char in char_range('a', 'z'):
        the_dictionnary.append({'letter' : char, 'occurences': book.count(char)})

    return the_dictionnary

def generate_report(book):
    print('Il y a ' + str(count_words(book)) + ' mots dans le livre.')
    letter_dictionary = count_every_letter(book)
    letter_dictionary.sort(reverse=True, key=sort_on)

    for count in letter_dictionary:
        print('Il y a ' + str(count['occurences']) + ' ' + count['letter'] +' dans le livre.')
        

generate_report(file_contents)