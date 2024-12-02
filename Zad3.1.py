numbers = [5,32,56,2,2,16,7,10,23,100]
mean_number = 0
max_number = 0
min_number = 0

for i in range(len(numbers)):
  numbers[i] = round(numbers[i] / 10) * 10

max_number = max(numbers)
min_number = min(numbers)

print(numbers)

numbers = [num for num in numbers if num != min_number and num != max_number]

print(numbers)

mean_number = sum(numbers) / len(numbers)
print(mean_number)