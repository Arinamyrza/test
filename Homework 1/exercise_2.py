#2)Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

def convert_to_preferred_format(sec):
    sec = int(input('Введите время в секундах: '))
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    print("количество часов:",hour)
    print("количество минут:",min)
    return "%02d:%02d:%02d" % (hour, min, sec)

n = 10000
print("время в формете :-", convert_to_preferred_format(n))
