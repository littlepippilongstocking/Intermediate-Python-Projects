"""
Dilyana Koleva, 2022
Intermediate Python Projects - Breadth First Search

If working on PyCharm don't forget to edit the configuration to emulate terminal in output console
Edit Configurations -> Click on the configuration -> Tick Emulate Terminal -> Apply

Also chances are the project won't run on PyCharm so run it directly through the terminal

"""
import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]


def print_maze(maze, screen, path=[]):
    CYAN = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                screen.addstr(i, j * 2, "X", RED)
            else:
                screen.addstr(i, j * 2, value, CYAN)


def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j

    return None


def find_path(maze, screen):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()

    while not q.empty():
        current, path = q.get()
        row, col = current

        screen.clear()
        print_maze(maze, screen, path)
        time.sleep(0.2)
        screen.refresh()

        if maze[row][col] == end:
            return path

        neighbours = find_neighbours(maze, row, col)
        for n in neighbours:
            if n in visited:
                continue

            r, c = n
            if maze[r][c] == "#":
                continue

            new_path = path + [n]
            q.put((n, new_path))
            visited.add(n)


def find_neighbours(maze, row, col):
    neighbours = []

    if row > 0:
        neighbours.append((row - 1, col))
    if row + 1 < len(maze):
        neighbours.append((row + 1, col))
    if col > 0:
        neighbours.append((row, col - 1))
    if col + 1 < len(maze[0]):
        neighbours.append((row, col + 1))

    return neighbours


def main(screen):
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)

    find_path(maze, screen)
    screen.getch()


wrapper(main)
