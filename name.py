name = input("Enter a name: ")
letter_count = {letter: name.count(letter) for letter in set(name)}
print(letter_count)