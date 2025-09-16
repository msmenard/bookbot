def count_words(text):
    separate_words = text.split()
    return len(separate_words)

def count_chars(text):
    characters = {}
    converted = text.lower()
    for char in converted:
        if char not in characters:
           characters[char] = 1
        else:
            characters[char] += 1
    return characters

def sort_on(items):
    return items["num"]

def sorted_list(character_dictionary):
    list_of_dictionaries = []
    for char in character_dictionary:
        indiv_char = {}
        indiv_char["char"] = char
        indiv_char["num"] = character_dictionary[char]
        list_of_dictionaries.append(indiv_char)
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    return list_of_dictionaries