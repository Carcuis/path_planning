import numpy as np
from point import Point
from common import Global


class RandomMap:
    def __init__(self, size=Global.map_size):
        self.obstacle_point_list = []
        self.size = size
        self.obstacle_count = size // 8
        # self.generate_obstacle()
        self.generate_y()

    def generate_obstacle(self):
        self.obstacle_point_list.append(Point(self.size // 2, self.size // 2))
        self.obstacle_point_list.append(Point(self.size // 2, self.size // 2 - 1))

        # Generate an obstacle in the middle
        for i in range(self.size // 2 - 4, self.size // 2):
            self.obstacle_point_list.append(Point(i, self.size - i))
            self.obstacle_point_list.append(Point(i, self.size - i - 1))
            self.obstacle_point_list.append(Point(self.size - i, i))
            self.obstacle_point_list.append(Point(self.size - i, i - 1))

        for i in range(self.obstacle_count - 1):
            x = np.random.randint(0, self.size)
            y = np.random.randint(0, self.size)
            self.obstacle_point_list.append(Point(x, y))

            if np.random.rand() > 0.5:  # Random boolean
                for l in range(self.size // 4):
                    self.obstacle_point_list.append(Point(x, y + l))
            else:
                for l in range(self.size // 4):
                    self.obstacle_point_list.append(Point(x + l, y))

    def is_obstacle(self, i, j):
        for p in self.obstacle_point_list:
            if i == p.x and j == p.y:
                return True
        return False

    def generate_y(self):
        for i in range(7):
            ''' (3, 17) -> (9, 11) '''
            self.obstacle_point_list.append(Point(3 + i, 17 - i))
        for i in range(6):
            ''' (3, 16) -> (8, 11) '''
            self.obstacle_point_list.append(Point(3 + i, 16 - i))
        for i in range(7):
            ''' (11, 11) -> (17, 17) '''
            self.obstacle_point_list.append(Point(11 + i, 11 + i))
        for i in range(6):
            ''' (12, 11) -> (17, 16) '''
            self.obstacle_point_list.append(Point(12 + i, 11 + i))

        for i in range(3):
            for j in range(8):
                ''' ((9, 10, 11), 3) -> ((9, 10, 11), 10) '''
                self.obstacle_point_list.append(Point(9 + i, 3 + j))
