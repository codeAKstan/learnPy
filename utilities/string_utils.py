# vowel count
vowels = ['a', 'e', 'i', 'o', 'u']

def vowel_count(word):
    count = 0
    for l in word:
        if l.lower() in vowels:
            count += 1
    return count
# reverse a string
def reverse_string(s):
    return s[::-1]
