import sys
import git

if __name__ == '__main__':
    repo = git.Repo(search_parent_directories=True)
    sha = repo.head.commit.hexsha
    print(repo.git.rev_parse(sha))
    #for line in sys.stdin:
        #print(line.replace("$Repo%", Repo.rev_parse()))


