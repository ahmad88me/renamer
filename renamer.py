import sys
import os

print sys.argv

if len(sys.argv) != 2:
    print "You should pass the name the of the directory"
    exit(1)

dir_name = sys.argv[1]
for filename in os.listdir(dir_name):
    if "." in filename:
        name_part = filename.split(".")[0]
        ext_part = "".join(filename.split(".")[1:])
        if name_part.isdigit() and int(name_part) < 10:
            new_name_part = "0"+str(int(name_part))
            os.rename(filename, new_name_part+"."+ext_part)




