with open('./books/frankenstein.txt') as f:
    file_contents = f.read()

def char_range(start, end):
    for character in range(ord(start), ord(end)):
        yield chr(character)

def count_words(book): 
    print(len(book.split()))

def count_every_letter(book):
    book = book.lower()
    the_dictionnary = {}
    for char in char_range('a', 'z'):
        the_dictionnary[char] = book.count(char)

    return the_dictionnary

print(count_every_letter(file_contents))
