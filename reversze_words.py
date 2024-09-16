def reverse_words(s):
    words = s.split()
    reversed_words = words[::-1]
    reversed_string = ' '.join(reversed_words)
    return reversed_string

input_string = "the sky is blue "
result = reverse_words(input_string)
print("Reversed string:", result)
