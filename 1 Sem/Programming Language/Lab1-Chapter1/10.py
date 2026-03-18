paragraph = input("Enter a paragraph: ")
paragraph_clean = paragraph.replace("!", ".").replace("?", ".")
sentences = paragraph_clean.split(".")
sentences = [s.strip() for s in sentences if s.strip()]
print("\nSentences:")
for i, s in enumerate(sentences, 1):
    print(f"{i}. {s}")
words = paragraph.split()
punctuation_chars = ".!?,;:"
clean_words = []
for w in words:
    while w and w[0] in punctuation_chars:
        w = w[1:]
    while w and w[-1] in punctuation_chars:
        w = w[:-1]
    if w:
        clean_words.append(w)
print("\nWords:")
for i, w in enumerate(clean_words, 1):
    print(f"{i}. {w}")