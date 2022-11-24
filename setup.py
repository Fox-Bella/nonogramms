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
COLOR_RED = "#FF4747"

square_game_sizes = []
for i in range(20):
    square_game_sizes.append(int(60 - i * 2.2))
level = 0

view_example = None
