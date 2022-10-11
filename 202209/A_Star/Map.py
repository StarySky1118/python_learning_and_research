# -*- coding:utf-8 -*-
from A_Star import Position
import queue


# 地图
class GameMap:
    map_matrix = []  # 地图矩阵
    map_length = 7  # 地图长度
    map_width = 5  # 地图宽度
    infinity = map_width + map_length + 1  # 无限距离

    # 构建地图：测试默认构建 5*7 的地图
    def __init__(self):
        for i in range(self.map_width):
            temp = []
            for j in range(self.map_length):
                temp.append(True)
            self.map_matrix.append(temp)

        self.map_matrix[1][3] = False
        self.map_matrix[2][3] = False
        self.map_matrix[3][3] = False

    # 结点是否可以前进
    def feasible(self, node: Position.Position):
        if node.x < 0 or node.x >= self.map_width:
            return False
        if node.y < 0 or node.y >= self.map_length:
            return False
        return self.map_matrix[node.x][node.y]

    # 可视化显示地图
    def show_map(self):
        for i in range(self.map_width):
            # for j in range(self.map_length):
            #     print(self.map_matrix[i][j], end="")
            # print()
            print(self.map_matrix[i])

    # A* 算法寻路
    '''
        思路分析：
            从源点开始，计算上下左右四个结点预估函数值，选择预估函数值小并且可行的点作为前进
            结点。
            
    '''

    def a_star_search(self, start: Position.Position, end: Position.Position):
        path_list = []  # 路径序列
        current_pos = start  # 当前位置
        while True:  # 在未到达最终目的地时进行寻路

            direction = 0  # 默认前进方向
            predicted_value = self.infinity  # 默认预估值

            # 确定行进方向
            for i in range(4):
                # 首先排除不可行进的结点
                adj_node = current_pos.adj_node(i)
                if self.feasible(adj_node):  # 该点必须可以前进
                    node_predicted_value = current_pos.predicted_value_detect(i, start, end)
                    if node_predicted_value < predicted_value:  # 探测值小于预估值
                        direction = i  # 记录方向
                        predicted_value = node_predicted_value  # 记录预估值

            # 根据前进方向移动
            path_list.append(Position.Position(current_pos.x, current_pos.y))  # 当前结点入队
            self.map_matrix[current_pos.x][current_pos.y] = False  # 设置地图矩阵值
            current_pos.move(direction)

            # 循环结束判断
            if current_pos.is_same(end):
                break

        return path_list
