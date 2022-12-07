from data.map import Map
class AddMap:

    def __init__(self):
        self.level = []

        self.level.append(Map("Квадрат", [[1, 1, 1],
                                          [1, 0, 1],
                                          [1, 1, 1]]))
        self.level.append(Map("Круг", [[0, 1, 1, 1, 0],
                                       [1, 0, 0, 0, 1],
                                       [1, 0, 0, 0, 1],
                                       [1, 0, 0, 0, 1],
                                       [0, 1, 1, 1, 0]]))
        self.level.append(Map("Солнце", [[1, 0, 0, 0, 1],
                                         [0, 1, 1, 1, 0],
                                         [0, 1, 1, 1, 0],
                                         [0, 1, 1, 1, 0],
                                         [1, 0, 0, 0, 1]]))
        self.level.append(Map("ТВ", [[1, 0, 0, 0, 1],
                                       [0, 1, 1, 1, 0],
                                       [1, 0, 0, 0, 1],
                                       [1, 0, 0, 0, 1],
                                       [0, 1, 1, 1, 0]]))
        self.level.append(Map("Дерево", [[1, 1, 1],
                                 [1, 1, 1],
                                 [1, 1, 1],
                                 [0, 1, 0],
                                 [0, 1, 0]]))
        self.level.append(Map("Гриб", [[0, 0, 1, 0, 0],
                                     [0, 1, 1, 1, 0],
                                     [1, 1, 1, 1, 1],
                                     [0, 0, 1, 0, 0],
                                     [0, 0, 1, 0, 0]]))
        self.level.append(Map("Роблокс", [[0, 0, 1, 0, 0],
                                     [0, 1, 1, 1, 0],
                                     [1, 1, 1, 1, 1],
                                     [0, 0, 1, 0, 0],
                                     [0, 0, 1, 0, 0]]))
        self.level.append(Map("Мишка", [[0, 1, 0, 1, 0],
                                 [0, 0, 1, 0, 0],
                                 [1, 1, 0, 1, 1],
                                 [0, 1, 1, 1, 0],
                                 [0, 1, 0, 1, 0]]))
        self.level.append(Map("Сердечко", [[0, 1, 0, 1, 0],
                                     [1, 1, 1, 1, 1],
                                     [1, 1, 1, 1, 1],
                                     [0, 1, 1, 1, 0],
                                     [0, 0, 1, 0, 0]]))
        self.level.append(Map("Улыбка", [[1, 1, 0, 1, 1],
                                     [0, 0, 0, 0, 0],
                                     [0, 1, 0, 1, 0],
                                     [0, 0, 1, 0, 0]]))
        self.level.append(Map("Моя любимая игрушка", [[1, 0, 0, 0, 1],
                                                     [0, 1, 1, 1, 0],
                                                     [0, 1, 1, 1, 0],
                                                     [1, 1, 1, 1, 1],
                                                     [0, 1, 1, 1, 0],
                                                     [0, 1, 1, 1, 0],
                                                     [0, 1, 0, 1, 0]]))
        self.level.append(Map("Сундук из маинкрафта", [[1, 1, 1, 1, 1],
                                                     [1, 0, 1, 0, 1],
                                                     [1, 0, 1, 0, 1],
                                                     [1, 0, 0, 0, 1],
                                                     [1, 1, 1, 1, 1]]))
        self.level.append(Map("Панда", [[1, 1, 0, 1, 1],
                                     [1, 0, 0, 0, 1],
                                     [0, 1, 0, 1, 0],
                                     [1, 0, 1, 0, 1],
                                     [1, 1, 0, 1, 1]]))
        self.level.append(Map("Котики", [[0, 0, 0, 0, 0, 0, 0, 1, 0],
                                         [0, 0, 0, 0, 0, 1, 1, 0, 1],
                                         [0, 0, 0, 0, 1, 1, 1, 1, 1],
                                         [0, 0, 0, 1, 1, 1, 1, 0, 1],
                                         [0, 0, 1, 1, 1, 1, 1, 1, 0],
                                         [0, 0, 1, 1, 1, 1, 1, 0, 1],
                                         [0, 1, 0, 1, 1, 1, 1, 1, 0],
                                         [0, 1, 0, 0, 0, 0, 0, 0, 0],
                                         [1, 1, 0, 0, 0, 0, 0, 0, 0]]))
        self.level.append(Map("Флаг", [[1, 1, 1, 1, 1, 1, 1, 1],
                                     [1, 1, 1, 1, 1, 1, 1, 1],
                                     [1, 1, 1, 1, 1, 1, 1, 1],
                                     [1, 1, 1, 1, 1, 1, 1, 1],
                                     [1, 1, 1, 1, 1, 1, 1, 1],
                                     [1, 0, 0, 0, 0, 0, 0, 0],
                                     [1, 0, 0, 0, 0, 0, 0, 0],
                                     [1, 0, 0, 0, 0, 0, 0, 0],
                                     [1, 0, 0, 0, 0, 0, 0, 0],
                                     [1, 0, 0, 0, 0, 0, 0, 0]]))
        self.level.append(Map("Весёлый камень", [[0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
                                                 [0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
                                                 [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
                                                 [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                                                 [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
                                                 [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]]))
        self.level.append(Map("Письмо", [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                     [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
                                     [1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
                                     [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
                                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]))
        self.level.append(Map("Телефон", [[1, 1, 1],
                                     [1, 1, 1],
                                     [0, 1, 1],
                                     [0, 1, 1],
                                     [0, 1, 1],
                                     [0, 1, 1],
                                     [0, 1, 1],
                                     [1, 1, 1],
                                     [1, 1, 1]]))
        self.level.append(Map("Крылья (свободы)", [[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                                     [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
                                     [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                                     [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                     [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                                     [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                                     [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
                                     [1, 1, 0, 0, 0, 0, 0, 0, 1, 1]]))
        self.level.append(Map("Бабочка", [[1, 1, 1, 0, 0, 0, 1, 1, 1],
                                     [1, 1, 1, 1, 0, 1, 1, 1, 1],
                                     [1, 1, 1, 1, 0, 1, 1, 1, 1],
                                     [1, 1, 1, 1, 1, 1, 1, 1, 1],
                                     [0, 0, 1, 1, 1, 1, 1, 0, 0],
                                     [0, 1, 1, 1, 1, 1, 1, 1, 0],
                                     [0, 1, 1, 1, 1, 1, 1, 1, 0]]))
        self.level.append(Map("Цветок спокойствия", [[0, 1, 1, 1, 0],
                                                     [1, 1, 0, 1, 1],
                                                     [1, 0, 1, 0, 1],
                                                     [1, 1, 0, 1, 1],
                                                     [0, 1, 1, 1, 0]]))
        self.level.append(Map("Рыбка", [[0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                                     [0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
                                     [1, 0, 0, 1, 1, 1, 1, 0, 1, 1],
                                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                     [1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
                                     [0, 1, 1, 1, 1, 1, 0, 0, 0, 1]]))
        self.level.append(Map("Дождливая ночь или Домик", [[0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
                                     [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                                     [0, 0, 1, 1, 1, 0, 1, 0, 0, 1],
                                     [0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                                     [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                                     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]))
        self.level.append(Map("Пончик", [[0, 1, 1, 1, 1, 1, 1, 0],
                                     [1, 1, 0, 1, 0, 0, 1, 1],
                                     [1, 1, 1, 1, 1, 0, 1, 1],
                                     [1, 0, 1, 0, 0, 1, 1, 1],
                                     [1, 0, 1, 0, 0, 1, 0, 1],
                                     [1, 1, 1, 1, 1, 1, 0, 1],
                                     [1, 0, 1, 0, 1, 0, 0, 1],
                                     [0, 1, 1, 1, 1, 1, 1, 0]]))
        self.level.append(Map("Морская свинка:))", [[0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                                     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                                     [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                                     [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                                     [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]))

