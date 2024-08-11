from datetime import date, datetime


def get_birthdays_per_week(users):
    #вказуэємо будні дні та вихідні.
    work_days = ['Monday', 'Tuesday', 'Wednesday','Thursday','Friday']
    weekends = ['Saturday', 'Sunday']
    birthdays = {}
    today = date.today() #отримуємо сьогоднішню дату
    #Перевірка на пустий список
    if users == []:
        return {}
    #Створюємо рамки тижня від сьогоднішньої дати та заносимо їх у масив
    time_zone = []
    count = 0 # лічильник на випадок, якщо кількість днів перевищила допустиму
    for j in range(0,7): # цикл довжиною у 7 днів
        try:
            week_count = datetime(today.year,today.month,today.day + j) # додаємо до сьогоднішнього дня сім днів
            time_zone.append(week_count) # кожинь день додається до списку
        except ValueError: # Якщо закінчується кількість днів у місяці.
            count = count + 1
            print(j)
            if today.month + 1 > 12: # якщо у разі, якщо закінчився рік
                week_count = datetime(today.year,1, 1)
                time_zone.append(week_count)
            else:
                week_count = datetime(today.year,today.month + 1, count) # переходимо на наступний місяць і починаємо новий розрахунок днів.
                time_zone.append(week_count)
    
    # у вхідному списку беремо ім'я і дату народження і зберігаємо у словнику birthdays
    for i in users:
        for keys,values in i.items():
            if keys == 'name':
                name = values.split(' ')
                name = name[0]
            elif keys == 'birthday':
                bday1 = values
                #bday = values.strftime('%A %d %B %Y')
                bday1 = datetime(today.year, bday1.month, bday1.day) # присвоюємо актуальний рік
                birthdays[name] = bday1
                print(bday1.day)
    users_1 = {'Monday':[],
             'Tuesday':[], 
             'Wednesday':[],
             'Thursday':[],
             'Friday':[]}
    users = {}
    print(birthdays)
    for key,b_day in birthdays.items(): # форматуэмо у відповідний формат
        if b_day in time_zone:
            if b_day.strftime('%A') in work_days: # якщо дата народження у робочі дні то додаємо її у цей день
                users_1[b_day.strftime('%A')].append(key) 
            elif b_day.strftime('%A') in weekends: # якщо дата випадаэ на вихідні, переноимо її на понеділок
                users_1['Monday'].append(key)
    for key,values in users_1.items(): # виводимо фінальний резултат без пустих днів.
        if users_1[key] == []:
            continue
        else:
            users[key] = values

    print(time_zone)
    print(users)                




    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 8, 11).date()},
        {"name": "Brandon Gachi", "birthday": datetime(1976, 8, 11).date()}
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
