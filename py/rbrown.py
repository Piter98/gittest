#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# rbrown.py

import random
import numpy as np
import matplotlib.pyplot as plt

def rbrowna():
    n = int(raw_input("Ile ruchów? "))
    x = y = 0
    lx = [x]
    ly = [y]

    for i in range(n):
        kat = random.randint(0, 360) * np.pi / 180
        x = x + np.cos(kat)
        y = y + np.sin(kat)
        lx.append(x)
        ly.append(y)

        print x,y
    s = np.sqrt(x**2 + y**2)
    print "Przesunięcie: ",s
    print lx, ly

    plt.plot(lx, ly, "o:", color="lime",linewidth="10")
    plt.legend(
            [u"Przesunięcie:" + str(s)],
            loc="upper left")
    plt.title("Ruchy Browna")
    plt.grid(True)
    plt.show()

def main(args):
    rbrowna()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
