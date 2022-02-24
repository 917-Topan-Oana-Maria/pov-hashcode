class RepoRelatii:
    def __init__(self):
        self._relation_list = []

    def add_to_repo(self, relation):
        self._relation_list.append(relation)

    @property
    def relation_list(self):
        return self._relation_list
