"""
Dilyana Koleva, July 2022
Intermediate Python Projects - Bulk Renamer
"""
import os


def main():
    i = 0
    path = "C:/Users/"  # choose your own path
    for filename in os.listdir(path):
        dest = "img" + str(i) + ".jpg"
        src = path + filename
        dest = path + dest
        os.renames(src, dest)
        i += 1


if __name__ == '__main__':
    main()
