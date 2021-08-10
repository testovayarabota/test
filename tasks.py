r, g, b = 'Red', 'Green', 'Blue'
print(r, b, g, r + g + b, b, g + b )

first_animal, second_animal = 'Заяц', 'Черепаха'
print(first_animal, 'спит,', second_animal, 'идёт')

first_name, last_name = input('Введите имя: '), input('Введите фамилию: ')
print("Вас зовут" '\n' + first_name, '\n' + last_name) 

first_name = input('Введите имя: ')
last_name = input('Введите фамилию: ')
city = input('Введите город проживания: ')
print('=' * 28)
print('Вас зовут', first_name, last_name)
print('Вы живете в городе', city)

greeting = 'Привет'
first_name = input('Введите имя пользователя: ')
intro = "К сожалению, у Вас нет доступа к системе."
info = "Пожалуйста, обратитесь к системному администратору."
print(greeting, first_name, '\n' + intro, '\n' + info)

first_city = input('Введите город вылета: ')
last_city = input('Введите город прилёта: ')
print(first_city, '--->', last_city)