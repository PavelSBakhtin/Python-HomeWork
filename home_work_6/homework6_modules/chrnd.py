from random import randint, shuffle
from .check import check_positions_ent
from .check import check_positions_rnd


def main_rnd(n):
    N = 8
    pos_line = list(range(1, 9))
    for _ in range(n):
        positions = []
        shuffle(pos_line)
        while not check_positions_rnd(pos_line, N):
            shuffle(pos_line)
        for i in range(1, 9):
            positions.append((i, pos_line[i - 1]))
        print(*positions)


if __name__ == '__main__':
    pass


# # Этот вариант работает, но очень долго:


# def creat_positions():
#     positions = []
#     for i in range(1, 9):
#         x, y = i, randint(1, 8)
#         positions.append((x, y))
#     return positions


# def main_rnd(n):
#     N = 8
#     for _ in range(n):
#         positions = creat_positions()
#         while not check_positions_ent(positions, N):
#             positions = creat_positions()
#         print(*positions)


# [(1, 1), (2, 6), (3, 8), (4, 3), (5, 7), (6, 4), (7, 2), (8, 5)]
