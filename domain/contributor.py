class Cont:
    def __init__(self, nume, skill):
        self._nume = nume
        self._skill = skill

    @property
    def nume(self):
        return self._nume

    @property
    def skill(self):
        return self._skill
