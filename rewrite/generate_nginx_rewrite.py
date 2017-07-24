import os
import re

urlexp = re.compile("url: (\S+)")

for filename in os.listdir("."):
    if filename[-3:] == ".md":
        with open(filename) as file:
            for line in file:
                m = urlexp.search(line)
                if m:
                    url = m.group(1)[:-1]
                    postname = filename[:-3]
                    print("rewrite ^{}$ /post/{}/ permanent;".format(url,postname))

