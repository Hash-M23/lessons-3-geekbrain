def main(first_name, last_name, year, city, email, phone):
    return f"{first_name} {last_name} ({year}), {city}, {phone}, {email}"


first_name = input("Введите имя")
last_name = input("Введите фамилию")
year = int(input("Год рождения"))
city = input("Город")
email = input("Мыло")
phone = input("Номер")

print(main(first_name, last_name, year, city, email, phone))