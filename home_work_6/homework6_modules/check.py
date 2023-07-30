def check_positions_ent(positions, N):
    for i in range(N):
        for j in range(i + 1, N):
            a, b = positions[i]
            c, d = positions[j]
            if a == c or b == d or abs(a - c) == abs(b - d):
                return False
    return True


def check_positions_rnd(positions, N):
    for i in range(N):
        for j in range(i + 1, N):
            if (positions[i] == positions[j] or
                positions[i] - i == positions[j] - j or
                positions[i] + i == positions[j] + j):
                return False
    return True
