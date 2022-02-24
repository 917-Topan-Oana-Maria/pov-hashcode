class Project:
    def __init__(self, name, duration, score, deadline, roles):
        self._name = name
        self._duration = duration
        self._score = score
        self._deadline = deadline
        self._roles = roles
        self._status = False

    @property
    def name(self):
        return self._name

    @property
    def duration(self):
        return self._duration

    @property
    def score(self):
        return int(self._score)

    @property
    def deadline(self):
        return self._deadline

    @property
    def roles(self):
        return self._roles

    @score.setter
    def score(self, value):
        self._score = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
