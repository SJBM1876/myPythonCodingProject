def reverse_words(text):
    words = text.split(' ')
    reversed_words = [word[::-1] for word in words]
    reversed_text = ' '.join(reversed_words)
    return reversed_text

input_text = str(input("Type a sentence you would like to be reversed: "))
result = reverse_words(input_text)
print(result)

