text = "banana"
freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

print(freq)  # {'b': 1, 'a': 3, 'n': 2}
