from .check import check_positions


def main():
    N = 8
    positions = []
    for i in range(1, 9):
        x, y = map(int, input(
            f'Введите координаты {i}-го ферзя через пробел: ').split())
        positions.append((x, y))
    print(f'\n{check_positions(positions, N)}')


if __name__ == '__main__':
    pass
