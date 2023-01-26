import sys
import re

for line in sys.stdin:
    print(re.sub(r"\$Repo:.*?\$", "$Repo$", line))
