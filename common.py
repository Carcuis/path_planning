import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from point import Point


class Global:
    map_size = 21
    start_point = Point(1, 1)
    end_point = Point(10, 14)

    @staticmethod
    def init_canvas(_map):
        plt.figure(figsize=(5, 5))

        current_axes = plt.gca()
        current_axes.set_xlim([0, _map.size])
        current_axes.set_ylim([0, _map.size])

        # draw grid and obstacle block
        for i in range(_map.size):
            for j in range(_map.size):
                if _map.is_obstacle(i, j):
                    current_axes.add_patch(Rectangle((i, j), width=1, height=1, color='gray'))
                else:
                    current_axes.add_patch(Rectangle((i, j), width=1, height=1, edgecolor='gray', facecolor='w'))

        # draw start and end point
        current_axes.add_patch(Rectangle(Global.start_point.get_coord(), width=1, height=1, facecolor='b'))
        current_axes.add_patch(Rectangle(Global.end_point.get_coord(), width=1, height=1, facecolor='r'))

        plt.axis('equal')
        plt.axis('off')
        plt.tight_layout()

        return current_axes

