def check_positions(positions, N):
    for i in range(N):
        for j in range(i + 1, N):
            a, b = positions[i]
            c, d = positions[j]
            if a == c or b == d or abs(a - c) == abs(b - d):
                return False
    return True
