def order(sentence):
    if not sentence:
        return ""
    
    words = sentence.split()

    word_number_pairs = []

    for word in words:
        number = int(''.join(filter(str.isdigit, word)))

        word_number_pairs.append((word, number))

    word_number_pairs.sort(key=lambda x: x[1])

    sorted_words = [pair[0] for pair in word_number_pairs]

    sorted_string = ' '.join(sorted_words)

    return sorted_string

input_string = input("Type a string containing numbers within the words: ")
sorted_result = order(input_string)
print(sorted_result)