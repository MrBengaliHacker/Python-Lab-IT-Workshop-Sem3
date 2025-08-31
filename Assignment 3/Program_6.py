text = input("Enter a string: ")

vowels = consonants = digits = special = 0
vowel_set = "aeiouAEIOU"

for ch in text:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        if ch in vowel_set:
            vowels += 1
        else:
            consonants += 1
    else:
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special Characters:", special)