import os

# get input folder
path = input("Where should we rename the volumes at? ")
to_remove = input("What extension to remove (do not omit the dot)? ")
# make sure it is a valid path
assert os.path.exists(path), "I did not find the folder at, " + str(path)
# convert to the os file path
files = os.listdir(path)


# defines function that returns filename without the designated extension
def rchop(s, suffix):
    if suffix and s.endswith(suffix):
        # chops the length of the provided suffix from string
        return s[:-len(suffix)]
    return s


for index, file in enumerate(files):
    x = rchop(file, to_remove)
    # renames the file
    os.rename(os.path.join(path, file), os.path.join(path, ''.join(x)))
