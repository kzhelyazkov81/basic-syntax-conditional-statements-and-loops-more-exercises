command = input()
coffee_needed = 0
extra_sleep = False

while command != 'END':
    if command in ('cat', 'dog', 'coding', 'movie'):
        coffee_needed += 1
    elif command in ('CAT', 'DOG', 'CODING', 'MOVIE'):
        coffee_needed += 2
    if coffee_needed > 5:
        extra_sleep = True
        break
    command = input()

if extra_sleep:
    print('You need extra sleep')
else:
    print(coffee_needed)
