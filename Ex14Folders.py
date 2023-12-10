import os
import random

names = ["Homer", "Marge", "Bart", "Lisa", "Maggie", "TestFolder"]


def filterd_dirs():
    global names

    dirs = [x[0][2:] for x in os.walk(".")]
    filterd_dirs = []

    for x in dirs:
        if x in names:
            filterd_dirs.append(x)

    return filterd_dirs


def create_folders():
    global names

    dirs = [x[0][2:] for x in os.walk(".")]

    filtered_dirs = filterd_dirs()

    while len(filtered_dirs) < len(names) and len(names) > 0:
        name = random.choice(names)

        if name not in filtered_dirs:
            os.mkdir(os.path.abspath(os.getcwd()) + "\\" + name)
            filtered_dirs = filterd_dirs()


def del_folders():
    global names

    for x in os.walk("."):
        s = x[0][2:]

        if s in names:
            os.removedirs(s)


if __name__ == "__main__":
    create_folders()
    # del_folders()
