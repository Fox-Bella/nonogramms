class Map:

    def __init__(self, name_level, data_level):
        self._name_level = name_level
        self._data_level = data_level

        if self.name_level == "":
            raise ValueError('Ошибка: нет имени уровня, работать не буду :(')

    @property
    def name_level(self):
        return self._name_level

    @property
    def data_level(self):
        return self._data_level
