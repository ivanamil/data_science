#code that generates samples from two distributions, and does linear regression to find boundar

import numpy as np
import matplotlib.pyplot as plt
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("c", "count", help="sample count", type=int)
    return parser.parse_args()


def norm_rasp(mu, sigma, count):
    s = np.random.normal(mu, sigma, (count, count))
    x = s[0][:]
    y = s[1][:]
    return x, y


def ring_transform(xy):
    res_z = []
    for z in xy:
        z = np.array(z)
        res_z.append(z/4 + z/np.linalg.norm(z))
    return res_z


if __name__ == "__main__":
    args = parse_args()

    x,y = norm_rasp(0, 0.5, args.count)
    plt.plot(x, y, 'x')
    #plt.show()

    xy = zip(x,y)
    #transform gaussian distribution to a ring distribution
    res_z = ring_transform(xy)

    zx,zy = zip(*res_z)
    plt.plot(zx, zy, 'x', color = 'r')
    plt.axis('equal')
    plt.show()
