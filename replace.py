import sys
import git

if __name__ == '__main__':
    remote_url = ""
    g = git.cmd.Git(".")
    lines = g.execute("git remote show origin").splitlines()
    for line in lines:
        if "Fetch" in line:
            remote_url = line.split(":",1)[-1]

    for line in sys.stdin:
        print(line.replace("$Repo%", "$Repo: %s%".format(remote_url)))
