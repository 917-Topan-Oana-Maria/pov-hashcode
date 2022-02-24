import random
class ServiceJanos:
    def __init__(self, repo, repo_relatii):
        self._repo = repo
        self._repo_relatii = repo_relatii

    @staticmethod
    def get_score(project):
        return (project.score/project.duration)

    def sort_by_score(self):
        self._repo.project_list.sort(key=self.get_score, reverse=True)

    # def sort_by_skill(self):
    #     self._repo.contributor_list.sort(key=self.get_score, reverse=True)

    def randomagarie(self):
        a= len(self._repo.project_list)
        b= len(self._repo.contributor_list)
        print (a)
        for i in self._repo.project_list:
            print(i.name)
            for j in i.roles:
                d=random.randint(0,b-1)
                print(self._repo.contributor_list[d].nume+" ",end="")
            print("\n",end="")



from Repo.Repo import Repo

repo= Repo("input.txt")
repo.read_from_file()
abc=ServiceJanos(repo,repo)
abc.randomagarie()