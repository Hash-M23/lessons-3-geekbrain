first_numbers = input("Введите число через пробел").split()
second_numbers = input("Введите второе число через пробел").split()

if "@" in second_numbers:
	second_numbers =second_numbers[:second_numbers.index("@")]

first_numbers.extend(second_numbers)

print(sum(map(int, first_numbers)))