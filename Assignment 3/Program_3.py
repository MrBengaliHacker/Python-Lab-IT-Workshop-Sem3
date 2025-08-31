text = input("Enter a sentence: ")

punctuation = ".,?!;:"

# remove punctuation
for p in punctuation:
    text = text.replace(p, "")

# split into words
words = text.split()

# count words
print("Sentence without punctuation:", text)
print("Number of words:", len(words))