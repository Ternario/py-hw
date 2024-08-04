# ---------------- Task 1 ---------------------

import sys
import os

get_arg = sys.argv

if os.path.exists(get_arg[1]):
    if os.path.isfile(get_arg[1]):

        if get_arg[1][-3:] == ".py":
            os.system(f"python {get_arg[1]}")
        else:
            print("Not a python file")

    else:
        print("Not a file")
else:
    print("File not found")


# ---------------- Task 2 ---------------------

import sys
import os

get_arg = sys.argv

os.chdir(get_arg[1])

print([(pathname, dirname, filename) for pathname, dirname, filename in os.walk(os.getcwd())])
