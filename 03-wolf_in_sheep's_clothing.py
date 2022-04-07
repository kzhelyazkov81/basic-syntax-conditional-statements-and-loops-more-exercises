animals = input()
animals_list = animals.split(', ')
n = len(animals_list)
sheep_number = 0

for i in range(n-1, -1, -1):
    if animals_list[n-1] == 'wolf':
        print('Please go away and stop eating my sheep')
        break
    else:
        if animals_list[i] == 'wolf':
            print(f'Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!')
            break
        else:
            sheep_number += 1
