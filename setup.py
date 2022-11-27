def load():
    ret = dict()
    try:
        f = open('setup.dat', 'r', encoding="UTF-8")
        data = f.readlines()
        f.close()
        for s in data:
            s = s.split("=")
            ret[s[0]] = s[1]
    except FileNotFoundError:
        f = open("setup.dat", "w", encoding="UTF-8")
        f.write("level=0\n")
        f.write("max_level=0\n")
        f.write(f"error=0\n")
        f.write(f"difficulty=0\n")
        f.write(f"hint=5\n")
        f.close()
        ret = load()

    return ret


def save():
    f = open("setup.dat", "w", encoding="UTF-8")
    f.write(f"level={level}\n")
    f.write(f"max_level={max_level}\n")
    f.write(f"error={error}\n")
    f.write(f"difficulty={difficulty}\n")
    f.write(f"hint={hint}\n")
    f.close()

# Ошибки - не больше трёх
# Подсказка - включает 1-3 незакрашенных поля
# Уровень, в конце выводится название фигуры
# Уровни игры - 1, 2, 3 (мало, средне, полностью)
# Следующий-предыдущий - только после прохождения
#
#
#

WIDTH = 1000
HEIGHT = 700
FPS = 120

# Цвет линий текста слева и сверху нонограммы
TEXT_COLOR = [(150, 190, 150), (150, 190, 50)]

# Подсветка текста
TEXT_LIGHT_BAD = "#A73737"
TEXT_LIGHT_GOOD = "#37A737"
TEXT_LIGHT_ATTENTION = "#936d36"

COLOR_WHITE = "#EFEFEF"
COLOR_DEEP_GRAY = "#373737"
COLOR_YELLOW = "#FFFF00"
COLOR_YELLOW_DARK = "#9d933a"
COLOR_RED = "#FF4747"

square_game_sizes = []
for i in range(20):
    square_game_sizes.append(int(60 - i * 2.2))

dataload = load()
level = int(dataload["level"])
max_level = int(dataload["max_level"])
difficulty = int(dataload["difficulty"])
error = int(dataload["error"])
hint = int(dataload["hint"])

view_example = None

# Данные для расчёта процентов скрытых выражениями чисел
percent_digits = [30, 60, 100]

