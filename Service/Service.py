class ServiceJanos:
    def __init__(self, repo, repo_relatii):
        self._repo = repo
        self._repo_relatii = repo_relatii

    @staticmethod
    def get_score(project):
        return project.score/project.deadline

    def sort_by_score(self):
        self._repo.project_list.sort(key=self.get_score, reverse=True)

