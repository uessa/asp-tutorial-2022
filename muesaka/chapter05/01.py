import numpy as np


def calc_a_lin(d, M, theta, f):
    c = 334
    p = np.zeros(M)
    a = np.zeros(M)
    u = [np.sin(theta), np.cos(theta), 0]

    for m in range(M):
        p[m] = [((m - 1) - ((M - 1) / 2)) * d, 0, 0]
        tmp = 1j * 2 * np.pi * f / c
        a[m] = np.exp(tmp * u * p[m])

    return a


if __name__ == "__main__":
    d = 0.05
    M = 3
    theta = 45
    f = 1000

    a = calc_a_lin(d, M, theta, f)
    print(d)
