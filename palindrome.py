def can_form_palindrome(string):
    char_count = {}
    
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
        if odd_count > 1:
            return "NO"
    
    return "YES"

input_string = "aabbccdd"
print(can_form_palindrome(input_string))
