# vector_list = [['a', 'k'],
#                ['k', 'c'],
#                ['k', 'b'],
#                ['b', 'd'],
#                ['c', 'd'],
#                ['d', 'e'],
#                ['e', 'f'],
#                ['e', 'g'],
#                ['f', 'd'],
#                ['f', 'h']]
import datetime
import random
import time
from contextlib import contextmanager

vector_list = []
for i in range(0, 100):
    random_nums = random.randint(1, 101)
    for j in range(0, 5):
        random_num1 = random.randint(2, 101)
        if str(random_nums) != str(random_num1):
            vector_list.append([str(random_nums), str(random_num1)])

"""
先把所有的矢量转化成一个字典集合
{"a": ["k"], 
"k": ["c", "b"], 
"b": ["d"], 
"c": ["d"], 
"d": ["e"], 
"e": ["f", "g"], 
"f": ["d", "h", "b"]}
"""
vector_dict = {}

for i in vector_list:
    if i[0] in vector_dict and i[1] not in vector_dict[i[0]]:
        vector_dict[i[0]].append(i[1])
    else:
        vector_dict[i[0]] = [i[1]]
print(vector_dict)
# 图形中有没有起点，有几个
start_list = []
end_list = []
for k in vector_dict:
    start_list.append(k)
    end_list += vector_dict[k]

# 如果只有起始节点不在终止节点中则为起点
tmp_list = []
for i in start_list:
    if i not in end_list:
        tmp_list.append(i)
print(f'起始点为：{tmp_list}')

# 如果只有终止节点不在起始节点中则为起点
tmp_list1 = []
for i in end_list:
    if i not in start_list:
        tmp_list1.append(i)
print(f'终止节点为：{tmp_list1}')


def has_ring(node, node_list):
    """
    :param node:
    :param node_list: 该路径所有的走过的节点
    :return:
    """
    if node in vector_dict:
        for item in vector_dict[node]:
            if item in node_list:
                node_list.append(item)

                print("重复的环状节点为: " + item + "，当前遍历节点: " + str("->".join(node_list)))
                # return item
            else:
                node_list_tmp = node_list.copy()
                node_list_tmp.append(item)
                return has_ring(item, node_list_tmp)

    else:
        print("可用的节点链条为: " + str("->".join(node_list)))
        return None


begin = datetime.datetime.now()
for i in tmp_list:
    tmp = has_ring(i, node_list=[i])
    if tmp:
        print(tmp)

end = datetime.datetime.now()
print(f"耗时{str((end-begin).seconds)} 秒")
