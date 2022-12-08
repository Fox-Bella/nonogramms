import random

import pygame

import setup
from setup import *
from engine.square import Square
from engine.horizontal import Horizontal
from engine.vertical import Vertical
from engine.errors.errors import Error
from engine.font import Font
from engine.screen.label_text import LabelText
from engine.screen.label_text_central import LabelTextCentral
from engine.errors.helper import Helper
from engine.screen.authors_text import AuthorsText
from sound.sound import Sound
from engine.screen.final_text import FinalText


class Game:
    PLAY_GAME = 0
    END_GAME = 1
    WIN_GAME = 2

    def __init__(self, maps, sound):
        self.gamestate = Game.PLAY_GAME

        # Текст с картинкой для победы или поражения
        self.final_text = None

        self.maps = maps
        self.sound = sound
        self.current_map = None
        self.fields = None
        self.i_line_cells = None
        self.j_line_cells = None
        self.size_field = None
        self.start_x = None
        self.start_y = None
        self.i_count_fields = None
        self.j_count_fields = None
        self.end_x = None
        self.end_y = None
        self.horizontal = None
        self.vertical = None
        self.fill = True
        self.blocked = True
        self.width = None
        self.height = None
        self.end_round_effect = None

        # Шрифт
        self.font = Font()

        # Вывод авторов
        self.authors = AuthorsText(self.font)

        # Вывод текстовых меток
        self.label_text = LabelText(self.font)

        # Считаем кадры, чтобы разгрузить процессор на проверках
        self.frame = 0

        # Чтобы не срабатывала ошибка дважды на одну и ту же клетку
        self.last_i = -1
        self.last_j = -1

        # Текст по окончании раунда или в случае ошибок
        self.label_text_central = None

        # Здесь анимация ошибок
        self.errors = []

        # Здесь анимация подсказок
        self.helper = []

        self.start_level()

    def clear_lists(self, l):
        if l is not None:
            for i in range(len(l) - 1, -1, -1):
                del l[i]
        return []

    def start_level(self):

        self.final_text = None

        # Сбросим надпись
        self.label_text_central = self.clear_lists(self.label_text_central)
        # Сбросим эффекты, если они были
        self.end_round_effect = self.clear_lists(self.end_round_effect)

        if setup.level >= len(self.maps.level):
            setup.reset()

        # Текущая карта
        self.current_map = self.maps.level[setup.level].data_level

        # Текущая карта с True или False
        # Самое коряво написанное, но быстрое копирование в Python
        self.fields = [f[:] for f in self.current_map]

        # Определение размера клетки в зависимости от их количества в окне
        self.size_field = square_game_sizes[max(len(self.fields), len(self.fields[0])) - 1]

        # Ширина и высота (в клетках) матрицы поля
        self.i_count_fields = len(self.current_map)
        self.j_count_fields = len(self.current_map[0])

        # Общая ширина и высота поля
        self.width = self.j_count_fields * self.size_field
        self.height = self.i_count_fields * self.size_field

        self.start_x = (795 - self.width) // 2
        self.start_y = (HEIGHT - self.height) // 2 + 100

        self.horizontal = Horizontal(self.current_map, self.start_x, self.start_y, self.size_field, self.font)
        self.vertical = Vertical(self.current_map, self.start_x, self.start_y, self.size_field, self.font)

        self.start_x = (795 - self.width + self.vertical.width) // 2
        self.start_y = (HEIGHT - self.height - self.horizontal.height) // 2 + 100

        self.end_x = self.start_x + self.size_field * self.j_count_fields
        self.end_y = self.start_y + self.size_field * self.i_count_fields

        # 780 - это граница, где начинаются кнопки
        self.start_y = (setup.HEIGHT - self.height + 50) // 2
        # self.start_x = (HEIGHT - self.vertical.width - self.height) // 2 + 100

        for i in range(len(self.fields)):
            for j in range(len(self.fields[i])):
                self.fields[i][j] = Square(self.start_x + j * self.size_field,
                                           self.start_y + i * self.size_field,
                                           self.size_field)
                # Раскомментировать, чтобы при загрузке показались все квадраты
                # self.fields[i][j].enabled = self.current_map[i][j]

        self.horizontal = Horizontal(self.current_map, self.start_x, self.start_y, self.size_field, self.font)
        self.vertical = Vertical(self.current_map, self.start_x, self.start_y, self.size_field, self.font)

        # Из скольки клеток состоят обведённые светлом блоки (3x3, 4x4, 5x5)
        marker = [1, 2, 3, 4, 5]
        for i in marker:
            if len(self.fields) % i == 0:
                self.i_line_cells = i
        for j in marker:
            if len(self.fields) % j == 0:
                self.j_line_cells = j

        if setup.error >= 8:
            self.end_game()

    def getCoord(self, j, i):
        if (j < self.start_x or j >= self.end_x or
                i < self.start_y or i >= self.end_y):
            return -1, -1

        i = min(len(self.fields) - 1, (i - self.start_y) // self.size_field)
        j = min(len(self.fields[0]) - 1, (j - self.start_x) // self.size_field)

        return j, i

    def set_blocked(self, j, i):
        j, i = self.getCoord(j, i)
        if j == -1 and i == -1:
            return False

        self.blocked = not self.fields[i][j].blocked

    def mouse_3_button_down(self, mouse, j, i):
        j, i = self.getCoord(j, i)
        if j == -1 and i == -1:
            return False
        self.fields[i][j].blocked = self.blocked

    def press_mouse_1(self, x, y):
        if not (self.vertical is None):
            self.vertical.press_mouse_1(x, y)
        if not (self.horizontal is None):
            self.horizontal.press_mouse_1(x, y)

    def act(self, deltatime, x, y):
        self.frame += 1
        if self.frame > 100000:
            self.frame = 1

        if not (self.vertical is None):
            self.vertical.check_mouse(x, y)
        if not (self.horizontal is None):
            self.horizontal.check_mouse(x, y)

        # Каждый 30-й кадр проверяем и удаляем неактивное
        if self.frame % 30 == 0:
            # Удаляем квадраты-ошибки
            for i in range(len(self.errors) - 1, -1, -1):
                if not self.errors[i].enabled:
                    del self.errors[i]

            # Удаляем квадраты-подсказки
            for i in range(len(self.helper) - 1, -1, -1):
                if not self.helper[i].enabled:
                    del self.helper[i]

            if not (self.label_text_central is None):
                for i in range(len(self.label_text_central) - 1, -1, -1):
                    if not self.label_text_central[i].enabled:
                        del self.label_text_central[i]

            if not (self.end_round_effect is None):
                for i in range(len(self.end_round_effect) - 1, -1, -1):
                    if not self.end_round_effect[i].enabled:
                        del self.end_round_effect[i]

    # Выводит на экран содержимое всех вложенных объектов классов
    def draw(self, scene: pygame, deltatime):

        """ ***** ИГРА ***********************************************************************"""
        if self.gamestate == Game.PLAY_GAME:

            for i in range(len(self.fields)):
                for j in range(len(self.fields[i])):
                    self.fields[i][j].drawIJ(scene, j, i, self.i_line_cells, self.j_line_cells)

            if self.end_round_effect is not None:
                for eff in self.end_round_effect:
                    eff.draw(scene, deltatime)

            # Выводим анимацию ошибок
            if len(self.errors) > 0:
                for err in self.errors:
                    err.draw(scene, deltatime)

            # Выводим клетки-подсказки
            if len(self.helper) > 0:
                for hlp in self.helper:
                    hlp.draw(scene, deltatime)

            pygame.draw.rect(scene, Square.color_fill, (self.start_x - 3, self.start_y - 3,
                                                        self.width + 6, self.height + 6), 1)
            if not (self.vertical is None):
                self.vertical.draw(scene)
            if not (self.horizontal is None):
                self.horizontal.draw(scene)

            """ ***** ПРОИГРЫШ *******************************************************************"""
        elif self.gamestate == Game.END_GAME:
            if self.final_text is not None:
                self.final_text.draw(scene, deltatime)

            """ ***** ПОБЕДА *********************************************************************"""
        elif self.gamestate == Game.WIN_GAME:
            if self.final_text is not None:
                self.final_text.draw(scene, deltatime)

        self.label_text.draw(scene)

        if self.label_text_central is not None:
            for ltc in self.label_text_central:
                ltc.draw(scene, deltatime)

    # Установка/переключатель заливки/удаления
    def set_filling(self, j, i):
        j, i = self.getCoord(j, i)
        if j == -1 and i == -1:
            return False

        self.fill = not self.fields[i][j].enabled

    # Нажатие мышкой по полю/клетке
    # Тут же считает и ошибки
    def mouse_1_button_down(self, mouse, j, i):
        j, i = self.getCoord(j, i)
        if j == -1 and i == -1:
            return False

        if self.fields[i][j].blocked:
            return False

        if mouse == 1:
            self.fields[i][j].enabled = self.fill

            if self.fill:
                if self.last_i != i or self.last_j != j:
                    self.last_i = i
                    self.last_j = j
                    if self.current_map[i][j] == 0:
                        self.sound.play(Sound.CLICK_BAD)
                        self.errors.append(Error(self.fields[i][j], FPS / 2))
                        setup.error += 1
                        self.fields[i][j].blocked = True
                        self.fields[i][j].enabled = False
                        self.last_i = -1
                        self.last_j = -1
                        if setup.error >= 8:
                            # Удаляем квадраты-ошибки
                            self.end_game()

    # Ищет подсказки: сравнивает каждую выключенную клетку с базой
    # Если в клетке нужно установить заливку, а её нет, то устанавливает
    # Количество определяется по формуле: количество незакрашенных клеток / 3, но не менее 1
    def run_help(self):
        if len(self.helper) > 0:
            return False
        if setup.hint == 0:
            return False

        clear_fields = []

        for i in range(len(self.current_map)):
            for j in range(len(self.current_map[i])):
                if self.current_map[i][j] == 1 and self.fields[i][j].enabled == False:
                    clear_fields.append([self.fields[i][j], i, j])

        if len(clear_fields) > 0:
            setup.hint -= 1

            random.shuffle(clear_fields)
            count = min(max(len(clear_fields) // 3, 1), 3)
            for i in range(count):
                self.helper.append(Helper(clear_fields[i][0], setup.FPS // 2))
                self.fields[clear_fields[i][1]][clear_fields[i][2]].enabled = True

    # Нажатие на кнопку "Проверить". Определяет, полностью ли собрана
    # головоломка или есть какие-то ошибки
    # В случае ошибок выводит их количество и предупреждение
    def check_end_round(self):
        count_clear = 0
        count_fill = 0
        count_blocked = 0
        for i in range(len(self.current_map)):
            for j in range(len(self.current_map[i])):
                if self.current_map[i][j] == 1 and not self.fields[i][j].enabled and self.fields[i][j].blocked:
                    count_blocked += 1
                elif self.current_map[i][j] == 1 and not self.fields[i][j].enabled:
                    count_fill += 1
                elif self.current_map[i][j] == 0 and self.fields[i][j].enabled:
                    count_clear += 1

        if count_fill + count_clear + count_blocked > 0:

            str_err_fill = self.choosePluralMerge(count_fill, "поле", "поля", "полей")
            str_err_clear = self.choosePluralMerge(count_clear, "поле", "поля", "полей")
            str_err_blocked = self.choosePluralMerge(count_blocked, "поле", "поля", "полей")

            string_out = ""
            if count_blocked > 0:
                string_out = f"Наобходимо разблокировать {str_err_blocked}"
            elif count_clear > 0 and count_fill > 0:
                string_out = f"Необходимо закрасить: {str_err_fill}, а {str_err_clear} очистить"
            elif count_clear > 0 and count_fill == 0:
                string_out = f"Необходимо очистить {str_err_clear}"
            elif count_clear == 0 and count_fill > 0:
                string_out = f"Необходимо закрасить {str_err_fill}"

            self.label_text_central.append(
                LabelTextCentral(setup.HEIGHT - 80, string_out, f"ERR{count_fill + count_clear + count_blocked}",
                                 setup.TEXT_LIGHT_BAD,
                                 self.font, setup.FPS * 3,
                                 2))
            self.sound.play(Sound.CLICK_BAD)
            setup.error += 1
            if setup.error >= 8:
                self.end_game()
        else:
            self.sound.play(Sound.UP_OR_DOWN)
            self.win_round()

    def choosePluralMerge(self, num, case_one, case_two, case_five):
        s = f"{num} "
        num = abs(num)
        if num % 10 == 1 and num % 100 != 11:
            s += case_one
        elif num % 10 >= 2 and num % 10 <= 4 and (num % 100 < 10 or num % 100 >= 20):
            s += case_two
        else:
            s += case_five

        return s

    def win_round(self):

        setup.max_level = max(setup.level + 1, setup.max_level)
        setup.max_level = min(setup.max_level, len(self.maps.level) - 1)
        setup.hint += 1
        if setup.hint > 25:
            setup.hint = 25

        if setup.level + 1 == len(self.maps.level):
            self.final_text = FinalText("Поздравляем! Вы победили!",
                                        "Отлично, вы собрали все сканворды в игре!",
                                        "png/win_game_cat.png", self.font, 0, 795)
            self.gamestate = Game.WIN_GAME

        else:

            text_win = 'Выберите пункт "Следующая" для продолжения'
            self.label_text_central.append(LabelTextCentral(setup.HEIGHT - 70, text_win, f"TEXTWIN",
                                                            setup.COLOR_GRAY,
                                                            self.font, setup.FPS * 10,
                                                            1))

            text_name_level = f'"{self.maps.level[setup.level].name_level}"'
            self.label_text_central.append(LabelTextCentral(setup.HEIGHT - 110, text_name_level, f"TEXTNAME",
                                                            setup.TEXT_LIGHT_GOOD,
                                                            self.font, setup.FPS * 20,
                                                            2))

        if len(self.end_round_effect) > 300:
            return False

        count = 0
        pause = setup.FPS
        line = 0
        increment = setup.FPS / 30
        for j in range(self.j_count_fields):
            for i in range(self.i_count_fields):
                if line % 2 == 0:
                    if self.current_map[i][j] == 1:
                        self.end_round_effect.append(Helper(self.fields[i][j], pause, int(count), 0, 100, 0))
                        count += increment

                    if self.current_map[self.i_count_fields - 1 - i][self.j_count_fields - 1 - j] == 1:
                        self.end_round_effect.append(
                            Helper(self.fields[self.i_count_fields - 1 - i][self.j_count_fields - 1 - j], pause,
                                   int(count), 0, 100, 0))
                        count += increment
                else:
                    if self.current_map[self.i_count_fields - 1 - i][j] == 1:
                        self.end_round_effect.append(
                            Helper(self.fields[self.i_count_fields - 1 - i][j], pause, int(count), 0, 100, 0))
                        count += increment

                    if self.current_map[i][self.j_count_fields - 1 - j] == 1:
                        self.end_round_effect.append(
                            Helper(self.fields[i][self.j_count_fields - 1 - j], pause, int(count), 0, 100, 0))
                        count += increment
            line += 1

    def draw_authors(self, scene, deltatime):
        self.authors.draw(scene, deltatime)

    # Конец игры / Ошибки
    def end_game(self):
        if self.errors is not None:
            for i in range(len(self.errors) - 1, -1, -1):
                del self.errors[i]
        self.errors = []

        # Удаляем квадраты-подсказки
        if self.helper is not None:
            for i in range(len(self.helper) - 1, -1, -1):
                del self.helper[i]
        self.helper = []

        if self.label_text_central is not None:
            for i in range(len(self.label_text_central) - 1, -1, -1):
                del self.label_text_central[i]
        self.label_text_central = []

        if self.end_round_effect is not None:
            for i in range(len(self.end_round_effect) - 1, -1, -1):
                del self.end_round_effect[i]
        self.end_round_effect = []

        self.sound.play(Sound.GAME_OVER)
        self.final_text = FinalText("Жаль, но вы проиграли...", "Вы допустили 8 ошибок. Нажмите \"Сбросить прогресс\" "
                                                                "чтобы начать заново",
                                    "png/game_over_cat.png", self.font, 0, 795)
        self.gamestate = Game.END_GAME
