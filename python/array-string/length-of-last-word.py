def last_word_length(s):
    pointer = len(s) - 1
    length = 0

    while pointer >= 0:
        if s[pointer] != ' ':
            length += 1
            pointer -= 1
        else:
            if length > 0:
                return length
            pointer -= 1

    return length


if __name__ == '__main__':
    s = "Hello World"
    print(last_word_length(s))

    s = "   fly me   to   the moon  "
    print(last_word_length(s))


