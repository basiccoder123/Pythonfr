def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr +=1
            lst.append(word)

    print("List of words with same character in them:", lst)
    return ctr

count = match_words(["xyz", "cfc", "ava", "aba", "1221", "323343", "4564", "6767"])
print("Number of words having first and last character same:", count)