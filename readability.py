def count_sentences(words):
    count_sentence = 0
    for i in words:
        if '.' in i or '!' in i or '?' in i:
            count_sentence += 1
    return count_sentence


def count_words(words):
    word = str(words).split(" ")
    return len(word)


def count_letters(words):
    letters = 0
    for i in words:
        if str(i).isalpha():
            letters += 1
    return letters


def grade(words):
    l = count_letters(words) * (100 / count_words(words))
    s = count_sentences(words) * (100 / count_words(words))
    index = 0.0588 * l - 0.296 * s - 15.8
    if index < 1:
        print("Before Grade 1")
    elif index > 16:
        print("Grade 16+")
    else:
        print(round(index))


grade("One fish. Two fish. Red fish. Blue fish.")
