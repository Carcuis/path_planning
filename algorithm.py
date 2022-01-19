import time
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from point import Point
from common import Global


class Algorithm:
    def __init__(self, _map, algorithm):
        """
        Initialize Algorithm

        :param _map: map contains obstacles
        :param algorithm: 0 (Dijkstra), 1 (Greedy Best First Search), 2 (A Star)
        """
        self.map = _map
        self.open_list = []
        self.close_list = []
        if algorithm not in (0, 1, 2):
            print("Algorithm must be 0 (Dijkstra) or 1 (Greedy Best First Search) or 2 (A Star).")
            exit(1)
        self.algorithm = algorithm

    @staticmethod
    def base_cost(p):
        """ Distance to start point """
        x_dis = abs(Global.start_point.x - p.x)
        y_dis = abs(Global.start_point.y - p.y)
        return x_dis + y_dis

    @staticmethod
    def heuristic_cost(p):
        """ Distance to end point """
        x_dis = abs(Global.end_point.x - p.x)
        y_dis = abs(Global.end_point.y - p.y)
        return x_dis + y_dis

    def total_cost(self, p):
        base_cost = self.base_cost(p) if self.algorithm != 1 else 0
        heuristic_cost = self.heuristic_cost(p) if self.algorithm != 0 else 0
        return base_cost + heuristic_cost

    def is_valid_point(self, x, y):
        if x < 0 or y < 0:
            return False
        if x >= self.map.size or y >= self.map.size:
            return False
        return not self.map.is_obstacle(x, y)

    @staticmethod
    def is_in_point_list(p, point_list):
        for _point in point_list:
            if _point.x == p.x and _point.y == p.y:
                return True
        return False

    def is_in_open_list(self, p):
        return self.is_in_point_list(p, self.open_list)

    def is_in_close_list(self, p):
        return self.is_in_point_list(p, self.close_list)

    @staticmethod
    def is_start_point(p):
        return p.x == Global.start_point.x and p.y == Global.start_point.y

    @staticmethod
    def is_end_point(p):
        return p.x == Global.end_point.x and p.y == Global.end_point.y

    @staticmethod
    def save_image():
        millis = int(round(time.time() * 1000))
        filename = './' + str(millis) + '.png'
        plt.savefig(filename)

    def process_point(self, x, y, parent):
        if not self.is_valid_point(x, y):
            return  # Do nothing for invalid point
        _point = Point(x, y)
        if self.is_in_close_list(_point):
            return  # Do nothing for visited point
        if not self.is_in_open_list(_point):
            _point.parent = parent
            _point.cost = self.total_cost(_point)
            self.open_list.append(_point)
        print(f'Process Point [{_point.x}, {_point.y}], cost: {_point.cost}')

    def select_point_in_open_list(self):
        cost_list = list(map(lambda i: i.cost, self.open_list))
        return -1 if not cost_list else cost_list.index(min(cost_list))

    def build_path(self, node, current_axes, start_time):
        path = []
        while True:
            # append from tail to start point
            if not self.is_end_point(node):
                path.append(node)
            node = node.parent
            if self.is_start_point(node):
                break

        # draw path
        for _node in path:
            rec = Rectangle((_node.x, _node.y), 1, 1, color='g')
            current_axes.add_patch(rec)
        end_time = time.time()
        print(f'===== Algorithm finish in {end_time - start_time} seconds')

    def run(self, current_axes):
        start_time = time.time()

        start_point = Global.start_point
        start_point.cost = 0
        self.open_list.append(start_point)

        while True:
            index = self.select_point_in_open_list()
            if index < 0:
                print('No path found, algorithm failed!!!')
                return
            node = self.open_list[index]
            rec = Rectangle((node.x, node.y), 1, 1, color='c')
            if not (self.is_start_point(node) or self.is_end_point(node)):
                current_axes.add_patch(rec)
                plt.text(node.x + 0.1, node.y + 0.2, node.cost)

            if self.is_end_point(node):
                return self.build_path(node, current_axes, start_time)

            self.open_list.pop(index)
            self.close_list.append(node)

            # Process all neighbors
            x = node.x
            y = node.y
            # self.process_point(x - 1, y + 1, node)
            self.process_point(x, y + 1, node)
            # self.process_point(x + 1, y + 1, node)
            self.process_point(x + 1, y, node)
            # self.process_point(x + 1, y - 1, node)
            self.process_point(x, y - 1, node)
            # self.process_point(x - 1, y - 1, node)
            self.process_point(x - 1, y, node)
