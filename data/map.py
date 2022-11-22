class Map:

    def __init__(self, name_level, data_level):
        self.name_level = name_level
        self.data_level = data_level

        if self.name_level == "":
            raise ValueError('Ошибка: нет имени уровня, работать не буду :(')
