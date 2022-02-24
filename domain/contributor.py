class Cont:
    def __init__(self, nume, skills):
        self._nume = nume
        self._skills = skills

    @property
    def nume(self):
        return self._nume

    @property
    def skills(self):
        return self._skills
