
# indeksi  0  1  2
numbers = [1, 2, 3, 5, 1, 3, 89, 12, 65, 23]

first_number = numbers[0]
print(first_number)

second_number = numbers[1]
print(second_number)

numbers.append(4)

fourth_number = numbers[3]
print(fourth_number)

print(numbers)

# sortED ne mijenja trajno listu
for number in sorted(numbers):
    print(number, end=' ')
print()

print(numbers)

# Trajno sort ira listu od manjeg prema vecem
numbers.sort()

print(numbers)

# Trajno sort ira listu od veceg prema manjem
numbers.sort(reverse=True)

print(numbers)