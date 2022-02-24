class Cont:
    def __init__(self, nume, skills):
        self._nume = nume
        self._skills = skills
        self._busy = 0

    @property
    def nume(self):
        return self._nume

    @property
    def skills(self):
        return self._skills
    @property
    def busy(self):
        return self._busy
    @busy.setter
    def busy(self, value):
        self._busy = value
