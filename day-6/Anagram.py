def is_anagram(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)


print(is_anagram("listen", "silent"))  
print(is_anagram("hello", "world"))    





# def is_anagram(s1: str, s2: str) -> bool:
#     return Counter(s1) == Counter(s2)
