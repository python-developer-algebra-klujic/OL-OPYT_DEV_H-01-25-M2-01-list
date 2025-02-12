numbers = []

for i in range(10):
    numbers.append(i)

print(numbers[5])
print()

numbers_length = len(numbers)
print('Duzina liste', numbers_length)
print()


# Krivi nacin ispisa liste
# print(numbers)
for number in numbers:
    print(number)
print()

numbers.insert(3, 'petsto')
print(numbers[5])

numbers_length = len(numbers)
print('Duzina liste', numbers_length)
print()

for number in numbers:
    print(number)
print()
