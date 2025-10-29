bash = 31
c_and_c_plus_plus = 29
c_sharp = 11
html_css = 36
java = 19
javascript = 37
sql = 34


def analyze_skills():
    # Соберём все значения в список, чтобы найти минимум и максимум
    skills = [
        bash,
        c_and_c_plus_plus,
        c_sharp,
        html_css,
        java,
        javascript,
        sql
    ]
    min_value = min(skills)
    max_value = max(skills)

    # Напечатаем требуемые строки
    print('Доля питонистов, у которых есть наименее популярный навык (в %):', min_value)
    print('Доля питонистов, у которых есть наиболее популярный навык (в %):', max_value)


# Не удаляйте вызов функции.
analyze_skills()