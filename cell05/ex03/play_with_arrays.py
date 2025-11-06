original_array = [2, 8, 9, 48, 8, 22, -12, 2]

processed_array_with_duplicates = []

for number in original_array:
    if number > 5:
        new_number = number + 2
        
        processed_array_with_duplicates.append(new_number)

final_unique_array = list(set(processed_array_with_duplicates))

print(original_array)
print(final_unique_array)