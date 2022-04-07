number = input()
biggest_number = ''
nums = sorted(list(number), reverse=True)

for i in range(len(nums)):
    biggest_number += nums[i]

print(biggest_number)
