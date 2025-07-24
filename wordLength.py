def countWordLength(s: str) -> int:
    count = 0
    i = len(s) - 1

    # Skip trailing spaces
    while i >= 0 and s[i] == ' ':
        i -= 1

    # Count characters of the last word
    while i >= 0 and s[i] != ' ':
        count += 1
        i -= 1

    return count

print(countWordLength("Hello World"))  # Output: 5
print(countWordLength("Python programming"))  # Output: 11
print(countWordLength("Test   "))  # Output: 4