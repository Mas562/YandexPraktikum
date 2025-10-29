from random import randint as rnd


def get_dumplings_recommendation(min_count, max_count):
    return rnd(min_count, max_count)


# При вызове указываем диапазон, в котором функция выберет случайное число.
# Например, если очень хочется есть — от 25 до 30 пельменей.
print('Оптимальным количеством пельменей на сегодня будет', get_dumplings_recommendation(25, 30))