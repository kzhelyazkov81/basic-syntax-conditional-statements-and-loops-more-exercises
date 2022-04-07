word = input()
word = word.lower()
new_word = ''
sand = 0
water = 0
fish = 0
sun = 0

for i in word:
    new_word += i
    if 'sand' in new_word:
        sand += 1
        new_word = ''
    elif 'water' in new_word:
        water += 1
        new_word = ''
    elif 'fish' in new_word:
        fish += 1
        new_word = ''
    elif 'sun' in new_word:
        sun += 1
        new_word = ''

sum = sand + water + fish + sun
print(sum)
