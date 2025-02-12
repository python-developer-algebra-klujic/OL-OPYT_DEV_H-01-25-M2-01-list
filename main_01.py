
# indeksi  0  1  2  3  4  5  6   7   8   9
numbers = [1, 2, 3, 5, 1, 3, 89, 12, 65, 23]

first_number = numbers[0]
print(first_number)

index = numbers.index(12) # vratit ce vrijednost indeksa 7 sto je index lokacije na kojoj
                            #je pohranjen element liste 12
numbers[index] = 15
numbers[7] = 15

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