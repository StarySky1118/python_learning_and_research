# -*- coding:utf-8 -*-
from A_Star.Map import GameMap
from A_Star.Position import Position
import queue

# game_map = GameMap()
# # print(game_map.map_matrix)
# game_map.show_map()

# p1 = Position(2, 1)
# p2 = Position(2, 5)
# print(Position.manhattan_distance(p1, p2))

# queue1 = queue.Queue(maxsize=0)
# queue1.put(1)
# queue1.put(2)
# queue1.put(3)
# queue1.put(4)
# print(queue1.get())
# print(queue1.get())
# print(queue1.get())
# print(queue1.qsize())
# print(queue1.queue)

# p1 = Position(2, 2)
# p2 = Position(2, 3)
# print(p1.is_same(p2))

current_pos = Position(2, 1)
start_pos = Position(2, 1)
dest_pos = Position(2, 5)

game_map = GameMap()

path_list = game_map.a_star_search(start_pos, dest_pos)

print()
# path_list = []
# path_list.append(1)
# path_list.append(2)
# print(path_list)

# print(Position.manhattan_distance(current_pos, dest_pos))

# for i in range(4):
#     node_name = ""
#     if i == 0:
#         node_name = "上方结点"
#     elif i == 1:
#         node_name = "右方结点"
#     elif i == 2:
#         node_name = "下方结点"
#     elif i == 3:
#         node_name = "左方结点"
#
#     print("{}预估值为{}".format(node_name, current_pos.predicted_value_detect(i, start_pos, dest_pos)))

# print(GameMap.a_star_search(start_pos, dest_pos))

# start_pos.show_pos()

# for i in range(4):
#     node_name = ""
#     if i == 0:
#         node_name = "上方结点"
#     elif i == 1:
#         node_name = "右方结点"
#     elif i == 2:
#         node_name = "下方结点"
#     elif i == 3:
#         node_name = "左方结点"
#
#     other = start_pos.adj_node(i)
#
#     print("起始结点的{}为{}".format(node_name, other.show_pos()))
