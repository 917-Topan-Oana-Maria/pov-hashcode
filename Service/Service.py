

class ServiceJanos:
    def __init__(self, repo, repo_relatii):
        self._repo = repo
        self._repo_relatii = repo_relatii

    @staticmethod
    def get_score(project):
        return (project.score/project.duration)+len(project.roles)

    def sort_by_score(self):
        self._repo.repo_project.sort(key=self.get_score, reverse=True)

    # def sort_by_skill(self):
    #     self._repo.contributor_list.sort(key=self.get_score, reverse=True)

    def assign(self):
        nr_projects = len(self._repo.repo_project)
        nr_contributor = len(self._repo.repo_contributors)
        self.sort_by_score()
        for i in range(0, nr_projects):
            nr_skills = len(self._repo.repo_project[i].roles)
            for j in range(0, nr_skills):
                for k in range(0, nr_contributor):
                    if self._repo.repo_contributors[k].busy is False and self._repo.repo_contributors[k].check_for_skill(self._repo.repo_project.roles[j]) is True:
                        self._repo.repo_contributors[k].busy = True
                        rel = Relatii(self._repo.repo_project[i].name, self._repo.repo_contributors[k].name)

                    pass
                pass

            pass




