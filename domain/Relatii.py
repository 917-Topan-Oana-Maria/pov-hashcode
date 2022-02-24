class Relatii:
    def __init__(self, name_project, name_contributor):
        self._name_project = name_project
        self._name_contributor = name_contributor

    @property
    def name_project(self):
        return self._name_project

    @property
    def name_contributor(self):
        return self._name_contributor
