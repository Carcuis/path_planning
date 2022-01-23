#!/usr/bin/env python3

import matplotlib.pyplot as plt
from random_map import RandomMap
from algorithm import Algorithm
from common import Global


def main():
    random_map = RandomMap()
    current_axes = Global.init_canvas(random_map)

    # use A star algorithm
    algorithm = Algorithm(random_map, 2)
    algorithm.run(current_axes)

    plt.show()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard interrupt.")
