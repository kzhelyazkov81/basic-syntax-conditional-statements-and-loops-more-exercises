word = input()
capital_letters_indices = []

for i in range(len(word)):
    if 64 < ord(word[i]) < 91:
        capital_letters_indices += [i]

print(capital_letters_indices)
