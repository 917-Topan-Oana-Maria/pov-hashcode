from domain.projects import Project
from domain.skills import Skill
from domain.contributor import Cont


class Repo:
    def __init__(self, filepath):
        self.repo_contributors = list()
        self.repo_project = list()
        self.__filepath = filepath

    def read_from_file(self):

        with open(self.__filepath, "r") as f:
            lines = f.readlines()
            n = len(lines)

            nr_cont = lines[0]
            lin = nr_cont.split(' ', maxsplit=1)
            nr_cont1 = int(lin[0])
            nr_project = int(lin[1])
            for line in range(1, n):
                if nr_cont1 > 0:
                    linie = lines[line].strip()

                    if len(linie) > 0:
                        parts = linie.split(' ')
                        name = parts[0]
                        nr_skills = int(parts[1])
                        list_skills = []
                        for skills in range(line + 1, line + nr_skills):
                            l = lines[skills].strip()
                            part = l.split(' ')
                            nume_skill = part[0]
                            lvl_skill = int(part[1])
                            sk = Skill(nume_skill, lvl_skill)
                            list_skills.append(sk)
                        contr = Cont(name, list_skills)
                        self.repo_contributors.append(contr)
                        line += nr_skills
                        nr_cont1 -= 1
                else:
                    linie = lines[line].strip()

                    if len(linie) > 0:
                        parts = linie.split(' ')
                        nume_project = parts[0]
                        zile = int(parts[1])
                        score = int(parts[2])
                        deadline = int(parts[3])
                        nr_roles = int(parts[4])
                        roles = []
                        for skills in range(line + 1, line + nr_roles):
                            r = lines[skills].strip()
                            part = r.split(' ')
                            nume_skill = part[0]
                            lvl_skill = int(part[1])
                            sk = Skill(nume_skill, lvl_skill)
                            roles.append(sk)
                        proj = Project(nume_project, zile, score, deadline, roles)
                        self.repo_project.append(proj)
                        line += nr_roles

    @property
    def project_list(self):
        return self.repo_project

    @property
    def contributor_list(self):
        return self.repo_contributors


abc = Repo()