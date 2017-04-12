#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import numpy as np

def rbrowna():
    n = int(raw_input("Ile ruchów? "))
    x = y = 0

    for i in range(n):
        kat = random.randint(0, 360) * np.pi / 180
        x = x + np.cos(kat)
        y = y + np.sin(kat)

        print x,y


def main(args):
    rbrowna()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
