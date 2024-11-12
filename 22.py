import collections

# Изначальный словарь питомцев
pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        },
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        },
    },
}

def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False

def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return 'год'
    elif 2 <= age % 10 <= 4 and not (12 <= age % 100 <= 14):
        return 'года'
    else:
        return 'лет'

def pets_list():
    for pet_id, pet_info in pets.items():
        for name, details in pet_info.items():
            print(f"ID: {pet_id}, Имя: {name}, Вид: {details['Вид питомца']}, "
                  f"Возраст: {details['Возраст питомца']} {get_suffix(details['Возраст питомца'])}, "
                  f"Имя владельца: {details['Имя владельца']}")

def create():
    last = collections.deque(pets, maxlen=1)[0]
    new_id = last + 1
    name = input("Введите имя питомца: ")
    pet_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца: ")
    
    pets[new_id] = {
        name: {
            "Вид питомца": pet_type,
            "Возраст питомца": age,
            "Имя владельца": owner_name
        },
    }
    print("Питомец добавлен!")

def read():
    pet_id = int(input("Введите ID питомца для просмотра информации: "))
    pet = get_pet(pet_id)
    if pet:
        for name, details in pet.items():
            print(f"Это {details['Вид питомца']} по кличке \"{name}\". "
                  f"Возраст питомца: {details['Возраст питомца']} {get_suffix(details['Возраст питомца'])}. "
                  f"Имя владельца: {details['Имя владельца']}")
    else:
        print("Питомец с таким ID не найден.")

def update():
    pet_id = int(input("Введите ID питомца для обновления информации: "))
    pet = get_pet(pet_id)
    if pet:
        name = list(pet.keys())[0]
        print(f"Текущая информация о питомце: {name}, {pet[name]}")
        pet_type = input("Введите новый вид питомца (оставьте пустым для пропуска): ")
        age = input("Введите новый возраст питомца (оставьте пустым для пропуска): ")
        owner_name = input("Введите новое имя владельца (оставьте пустым для пропуска): ")
        
        if pet_type:
            pet[name]["Вид питомца"] = pet_type
        if age:
            pet[name]["Возраст питомца"] = int(age)
        if owner_name:
            pet[name]["Имя владельца"] = owner_name
        
        print("Информация о питомце обновлена!")
    else:
        print("Питомец с таким ID не найден.")

def delete():
    pet_id = int(input("Введите ID питомца для удаления: "))
    if pet_id in pets:
        del pets[pet_id]
        print("Питомец удален!")
    else:
        print("Питомец с таким ID не найден.")

# Основной цикл программы
command = ""
while command != "stop":
    command = input("Введите команду (create, read, update, delete, list, stop): ").strip().lower()
    if command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "list":
        pets_list()
    elif command == "stop":
        print("Выход из программы.")
    else:
        print("Неизвестная команда. Пожалуйста, попробуйте снова.")
