import numpy as np


def calc_a_cir(r, M, theta, f):
    c = 334
    p = np.zeros(M)
    a = np.zeros(M)
    u = [np.sin(theta), np.cos(theta), 0]

    for m in range(M):
        tmp_p1 = r * np.sin(2 * np.pi / M * (m - 1))
        tmp_p2 = r * np.cos(2 * np.pi / M * (m - 1))
        p[m] = [tmp_p1, tmp_p2, 0]
        tmp = 1j * 2 * np.pi * f / c
        a[m] = np.exp(tmp * u * p[m])

    return a


if __name__ == "__main__":
    r = 0.05
    M = 3
    theta = 45
    f = 1000

    a = calc_a_cir(r, M, theta, f)
    print(a)
