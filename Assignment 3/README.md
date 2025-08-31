## 📋Program 1: Word Frequency in a Paragraph

**Question**: Write a Python program that reads a paragraph from the user and prints the frequency of each word in it.

**Solution**: [View Code](Program_1.py)

```python
paragraph = input("Enter a paragraph: ")

words = paragraph.lower().split()
frequency = {word:words.count(word) for word in set(words)}

print("Work frequency: ")
for word, count in frequency.items():
    print(word, ":", count)
```
### OUTPUT

```
Enter a paragraph: Python is easy and Python is powerful
Word frequency: 
powerful : 1    
python : 2      
is : 2
and : 1
easy : 1 
```

## 📋Program 2: String Encryption (Shift by 3)

**Question**: Write a Python program to encrypt a string by shifting each character by 3 positions in the alphabet.
(For example: A → D, B → E, X → A, etc.)

**Solution**: [View Code](Program_2.py)

```python
text = input("Enter a string: ")

# Create an empty string to store encrypted text
encrypted_text = ""

for char in text:
    if char.isalpha():   # Check if the character is a letter (A-Z or a-z)
        
        if char.isupper():  # If the character is UPPERCASE
            encrypted_text += chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
        
        else:  # If the character is LOWERCASE
            encrypted_text += chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
    
    else:
        # If it's not a letter (like number, space, symbol), keep it as it is
        encrypted_text += char  

print("Encrypted string:", encrypted_text)
```
### OUTPUT

```
Enter a string: ABC xyz
Encrypted string: DEF abc
```
```
Enter a string: Hello World
Encrypted string: Khoor Zruog
```

## 📋Program 3: Remove Punctuation and Count Words

**Question**: Write a Python program to remove all punctuation (.,?!;: etc.) from a string and count the number of words.

**Solution**: [View Code](Program_3.py)

```python
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
```
### OUTPUT

```
Enter a sentence: Hello, how are you?
Sentence without punctuation: Hello how are you
Number of words: 4
```
```
Enter a sentence: Hello, world! Python is great.
Sentence without punctuation: Hello world Python is great
Number of words: 5
```

## 📋Program 4: Longest Word in a Sentence

**Question**: Write a Python function that finds and prints the longest word in a given sentence.

**Solution**: [View Code](Program_4.py)

```python
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Assume the first word is the longest
longest_word = words[0]

# Check each word
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("The longest word is:", longest_word)
print("Length of the word:", len(longest_word))
```
### OUTPUT

```
Enter a sentence: Python programming is fun
The longest word is: programming
Length of the word: 11
```

## 📋Program 5: Strong or Weak Password

**Question**: Write a Python program to check whether a password is strong or weak.
Conditions for strong password:

At least 8 characters

Contains at least one uppercase letter

Contains at least one lowercase letter

Contains at least one digit

Contains at least one special character (@, #, $, %, &, *)

**Solution**: [View Code](Program_5.py)

```python
import re

password = input("Enter a password: ")

if (len(password) >= 8 and
    re.search(r"[A-Z]", password) and
    re.search(r"[a-z]", password) and
    re.search(r"[0-9]", password) and
    re.search(r"[@#$%&*]", password)):
    print("Strong Password")
else:
    print("Weak Password")

```
### OUTPUT

```
Enter a password: ritam123
Weak Password 
```
```
Enter a password: Ritam@123
Strong Password
```

## 📋Program 6: Count Vowels, Consonants, Digits, and Special Characters

**Question**: Write a program that takes a string and counts:

Number of vowels

Number of consonants

Number of digits

Number of special characters

**Solution**: [View Code](Program_6.py)

```python
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
```
### OUTPUT

```
Enter a string: Ritam@123
Vowels: 2
Consonants: 3
Digits: 3
Special Characters: 1 
```