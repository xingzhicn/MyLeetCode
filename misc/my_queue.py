def bar(input_queue: list):
    """
    “输入队列是[1,2,3,4]，按照如下步骤输出队列：
    1.将输入头部元素移到输出队列的尾部
    2.将输入头部元素移到输入队列尾部，重复1-2步骤直到没有输入队列为空，根据输出队列还原输入队列”
    """
    result = []
    for i in range(len(input_queue)):
        # 将输入队列尾部放到输入头部元素
        if result:
            tmp1 = result.pop()
            result.insert(0, tmp1)
        # 将输出尾部元素移到输入队列的头部
        tmp = input_queue.pop()
        result.insert(0, tmp)

    return result


def foo(input_queue: list):
    """
    原函数
    :param input_queue:
    :return:
    """
    result = []

    while input_queue:
        # 将输入头部元素移到输出队列的尾部
        tmp = input_queue.pop(0)
        result.append(tmp)
        # 将输入头部元素移到输入队列尾部
        if input_queue:
            tmp1 = input_queue.pop(0)
            input_queue.append(tmp1)
    return result


assert bar(foo([1, 2, 3, 4, 5, 6, 7, 8, 9])) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
