# 1. Print characters at prime index positions in a string
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("\n1. Characters at prime index positions:")
s = "helloworld"
for i in range(len(s)):
    if is_prime(i):
        print(f"Index {i}: {s[i]}")

# 2. Print the word with the largest length in a sentence
print("\n2. Word with largest length:")
sentence = "Python makes coding very interesting"
words = sentence.split()
largest = max(words, key=len)
print("Largest word:", largest)

# 3. Reverse a given string
print("\n3. Reverse a string:")
s = "OpenAI"
print("Reversed string:", s[::-1])

# 4. Print only vowel characters at even order positions
print("\n4. Vowels at even order positions:")
s = "education"
vowels = "aeiouAEIOU"
for i in range(len(s)):
    if (i + 1) % 2 == 0 and s[i] in vowels:
        print(s[i])

# 5. Frequency of each character (without count())
print("\n5. Frequency of characters:")
s = "programming"
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
for k, v in freq.items():
    print(k, ":", v)
