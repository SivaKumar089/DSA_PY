def is_anagram(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)

# Test
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False



# from collections import Counter

# def is_anagram(s1: str, s2: str) -> bool:
#     return Counter(s1) == Counter(s2)
