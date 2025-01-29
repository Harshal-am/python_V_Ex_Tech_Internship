#task 1: Loop Through a List
# Task 1
numbers = [10, 20, 30, 40, 50]

# Loop through the list and print each number multiplied by 2
print("Numbers multiplied by 2:")
for num in numbers:
    print(num * 2)

total_sum = sum(numbers)
print("Sum of all numbers:", total_sum)

#Task : 2 List Comprehension
# Original list of numbers
numbers = [5, 12, 17, 24, 35]

filtered_numbers = [num for num in numbers if num > 15]

squared_numbers = [num ** 2 for num in filtered_numbers]


print("Filtered list (numbers > 15):", filtered_numbers)
print("Squared list:", squared_numbers)

#task :3 : Create and manipulate lists.
fruits = ["apple", "banana", "cherry", "date"]

fruits.append("orange")

# Insert "grape" at index 2 using insert()
fruits.insert(2, "grape")

fruits.remove("date")
print("Final list:", fruits)

#Task:4 Sort Lists
numbers = [42, 12, 89, 33, 7]
numbers.sort()
print("Ascending Order:", numbers)

numbers.sort(reverse=True)
print("Descending Order:", numbers)

numbers.reverse()
print("Reversed List:", numbers)

#task:5 Sort List Alphanumerically
names = ["Emma", "Olivia", "Liam", "Noah", "Sophia"]

# Sorting alphabetically
names.sort()
print("Alphabetical Order:", names)

names.sort(reverse=True)
print("Reverse Alphabetical Order:", names)

names.append("James")
names.sort()
print("After Adding 'James' and Sorting:", names)

#task:6 Descending Order
numbers = [50, 10, 70, 30, 90]

numbers.sort(reverse=True)
print("Sorted Numbers (Descending Order):", numbers)

animals = ["dog", "cat", "zebra", "elephant", "ant"]
animals.sort(reverse=True)
print("Sorted Strings (Reverse Alphabetical Order):", animals)
