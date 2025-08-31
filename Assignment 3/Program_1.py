paragraph = input("Enter a paragraph: ")

words = paragraph.lower().split()
frequency = {word:words.count(word) for word in set(words)}

print("Word frequency: ")
for word, count in frequency.items():
    print(word, ":", count)