# -*- coding:utf-8 -*-
# 位置类
class Position:
    x = 0
    y = 0

    # 构造函数
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 计算曼哈顿距离
    @staticmethod
    def manhattan_distance(p1, p2):
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)

    # 判断位置是否相同
    def is_same(self, other):
        return self.x == other.x and self.y == other.y

    # 显示当前位置
    def show_pos(self):
        return "[{},{}]".format(self.x, self.y)

    # 根据方向移动
    def move(self, direction: int):
        if direction == 0:
            self.x -= 1
        elif direction == 1:
            self.y += 1
        elif direction == 2:
            self.x += 1
        elif direction == 3:
            self.y -= 1

    # def move_up(self):
    #     self.y -= 1
    #
    # def move_down(self):
    #     self.y += 1
    #
    # def move_right(self):
    #     self.x += 1
    #
    # def move_left(self):
    #     self.x -= 1

    # 返回当前结点的上、右、下或者左结点
    def adj_node(self, direction: int):
        if direction == 0:
            other = Position(self.x - 1, self.y)
        elif direction == 1:
            other = Position(self.x, self.y + 1)
        elif direction == 2:
            other = Position(self.x + 1, self.y)
        elif direction == 3:
            other = Position(self.x, self.y - 1)

        return other

    # 探测上、右、下、左侧结点的曼哈顿距离值
    # direction = 0, 1, 2, 3 分别表示 向上、向右、向下、向左
    def predicted_value_detect(self, direction: int, start, dest):
        # 获取邻接结点
        other = self.adj_node(direction)

        return Position.manhattan_distance(start, other) + Position.manhattan_distance(dest, other)
