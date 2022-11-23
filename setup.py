WIDTH = 900
HEIGHT = 600
FPS = 120

# Цвет линий текста слева и сверху нонограммы
TEXT_COLOR = [(150, 190, 150), (150, 190, 50)]

# Подсветка текста
TEXT_LIGHT_BAD = "#A73737"
TEXT_LIGHT_GOOD = "#37A737"

COLOR_WHITE = "#EFEFEF"
COLOR_YELLOW = "#FFFF00"
COLOR_RED = "#FF4747"

square_game_sizes = []
for i in range(20):
    square_game_sizes.append(int(60 - i * 2.2))
level = 0

view_example = None
