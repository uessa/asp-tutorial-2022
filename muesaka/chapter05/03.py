import numpy as np


def calc_a(r, M, theta, f):
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


def calc_a_nor(arr_p, theta, f):
    c = 334
    M = arr_p.shape[0]
    tmp_arr_x = 0
    tmp_arr_y = 0
    for i in range(M):
        tmp_arr_x += arr_p[i][0]
        tmp_arr_y += arr_p[i][1]
    tmp_arr_x = tmp_arr_x / M
    tmp_arr_y = tmp_arr_y / M

    p = np.zeros(M)
    a = np.zeros(M)
    u = [np.sin(theta), np.cos(theta), 0]

    for m in range(M):
        tmp_p1 = tmp_arr_x * np.sin(2 * np.pi / M * (m - 1))
        tmp_p2 = tmp_arr_y * np.cos(2 * np.pi / M * (m - 1))
        p[m] = [tmp_p1, tmp_p2, 0]
        tmp = 1j * 2 * np.pi * f / c
        a[m] = np.exp(tmp * u * p[m])

    return a


if __name__ == "__main__":
    theta = 45
    f = 1000
    arr = [[1, 2, 0], [2, 2, 0]]
    arr = np.array(arr)
    a = calc_a_nor(arr, theta, f)
    print(a)
