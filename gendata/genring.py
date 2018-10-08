#code that generates samples from two distributions, and does linear regression to find boundar

import numpy as np
import matplotlib.pyplot as plt

def norm_rasp(mu,sigma):
    s = np.random.normal(mu, sigma, (100, 100))
    x = s[0][:]
    y = s[1][:]
    return x,y

def ring_transform(xy):
    res_z = []
    for z in xy:
        z = np.array(z)
        res_z.append(z/4 + z/np.linalg.norm(z))
    return res_z

x,y = norm_rasp(0,0.5)
plt.plot(x, y, 'x')
#plt.show()

xy = zip(x,y)
#transform gaussian distribution to a ring distribution
res_z = ring_transform(xy)

zx,zy = zip(*res_z)
plt.plot(zx, zy, 'x', color = 'r')
plt.axis('equal')
plt.show()

#linear classifier

#X_all = np.append(x,zx)
#Y_all = np.append(y,zy)

#beta = np.linalg.inv(X_all.T * X_all) * X_all.T * Y_all