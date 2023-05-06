# DashInsert

def DashInsert(nums):
    i = 0
    result = []
    
    while i < len(nums) - 1:
        result.append(nums[i])
        if int(nums[i]) % 2 == 0 and int(nums[i + 1]) % 2 == 0:
            result.append('*')
        elif int(nums[i]) % 2 == 1 and int(nums[i + 1]) % 2 == 1:
            result.append('-')
        i += 1
    result.append(nums[i])

    return result

    numbers = list(map(int, nums))
    result = []

    for i, num in enumerate(numbers):
        result.append(str(num))
        if i < len(numbers) - 1:
            is_odd = num % 2 == 1
            is_next_odd = numbers[i + 1] % 2 == 1
            if is_odd and is_next_odd:
                result.append('-')
            elif not is_odd and not is_next_odd:
                result.append('*')
    return result

numbers = input()
print(''.join(DashInsert(numbers)))
