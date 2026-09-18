sentence = input("Enter a sentence: ")

words = sentence.lower().split()

unique_words = set(words)

print("Unique words:", unique_words)
print("Total unique words:", len(unique_words))