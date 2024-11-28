words = ["level","world","madam","python","racecar","java"]
palindrome = list(filter(lambda word: word == word[::-1],words))
print(palindrome)
