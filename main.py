import sys
import git

if __name__ == '__main__':
    repo = git.Repo(search_parent_directories=True)
    git_root = repo.git.rev_parse("--show-toplevel")
    print(repo.remote().urls())
    print(git_root)
    name = git_root.split('/')[-1]
    print(name)
    #for line in sys.stdin:
        #print(line.replace("$Repo%", Repo.rev_parse()))
