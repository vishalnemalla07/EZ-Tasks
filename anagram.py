def are_anagrams(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    return sorted_str1 == sorted_str2

if __name__ == "__main__":
    str1 = input().strip()
    str2 = input().strip()
    result = are_anagrams(str1, str2)
    print(result)
