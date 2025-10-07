from collections import Counter

def find_anagrams(s, p):
    result = []
    p_count = Counter(p)
    window = Counter(s[:len(p)])

    if window == p_count:
        result.append(0)

    for i in range(len(p), len(s)):
        window[s[i]] += 1             # add new char
        window[s[i - len(p)]] -= 1     # remove old char

        if window[s[i - len(p)]] == 0:
            del window[s[i - len(p)]]

        if window == p_count:
            result.append(i - len(p) + 1)

    return result


s = "cbaebabacd"
p = "abc"
print("Anagram indices:", find_anagrams(s, p))
