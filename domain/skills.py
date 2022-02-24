class Skill:
    def __init__(self, name, level):
        self._name = name
        self._level = level

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value