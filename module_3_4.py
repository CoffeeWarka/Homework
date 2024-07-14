def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        i_lower = i.casefold()
        root_word_lower = root_word.casefold()
        if root_word_lower.__contains__(i_lower) or i_lower.__contains__(root_word_lower):
            same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)