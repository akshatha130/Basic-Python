#python program to count the each vowels in a Word and find the length of string.
a = input("Enter a character: ")
b_dict = dict()
vowels = "aeiouAEIOU"  # Vowels in both lowercase and uppercase

for b in a:
    if b in vowels:  # Checks if the character is a vowel
        count = a.count(b)
        b_dict[b] = count

print('Vowel Count:', b_dict)
print('Length:', len(a))
