def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                if numbers[i] + numbers[j] == target:
                    return i, j