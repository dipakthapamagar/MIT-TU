text = input("Enter a string: ")
text_lower = text.lower()
vowels = 0
consonants = 0
vowel_letters = "aeiou"
for char in text_lower:
    if char.isalpha():
        if char in vowel_letters:
            vowels += 1
        else:
            consonants += 1
print("\nCounts in the given string:")
print("Vowels:", vowels)
print("Consonants:", consonants)