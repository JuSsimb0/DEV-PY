numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

count_of_list = len(numbers)
for i in range(count_of_list):
    if numbers[i] is None:
        index_of_None = i
numbers[index_of_None] = (sum(numbers[:index_of_None]) + sum(numbers[index_of_None + 1:])) / count_of_list

print("Измененный список:", numbers)
