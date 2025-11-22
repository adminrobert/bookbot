
def get_num_words(text):
    words = text.split()
    return len(words)
    
def get_char_count(text: str):
    chars = {}
    for char in text:
        lc = char.lower()
        if lc in chars:
            chars[lc] += 1
        else:
            chars[lc] = 1
    return chars

def obj_sort(items):
    return items["nums"]

def sorted_char_count(chars):
    to_sort = []
    for pair in chars.items():
        to_sort.append({"char": pair[0], "nums": pair[1]})
    to_sort.sort(reverse=True, key=obj_sort)
    return to_sort