# -*- coding: utf-8 -*-
from linkedlist import Node

class LinkedListQueue:
    def __init__(self):
        """构造函数，注意无capacity的概念"""
        self._head = None       # 首节点，初始化为None
        self._tail = None       # 尾节点，初始化为None
        self._size = 0           # 有效元素的个数，初始化为0

    def getSize(self):
        """
        获取队列中有效元素的个数
        :return: 元素个数
        """
        return self._size

    def isEmpty(self):
        """
        判断队列是否为空
        :return: Bool值，空为True
        """
        return self._size == 0

    def enqueue(self, elem):
        """
        将元素elem入队，注意是在self._tail处进行入队操作
        时间复杂度：O(1)
        :param elem: 将要入队的元素，需要用一个Node来装载它
        """

        if self.isEmpty():  # 控队列需要特殊处理
            # 此时队列为空，则self._tail为None，此时self._head一定也是None
            # 因为绝对不存在self._tail为None，而self._head不是空的情况
            self._tail = Node(elem)  # 将self._tail设为携带elem，且下一个元素为None的一个节点
            self._head = self._tail  # 将self._head置为self._tail，即self._head和self._tail标签同时贴在了这一个Node上，这样就把self._head和self._tail关联起来了

        else:
            self._tail.next = Node(elem)  # 如果不为空正常在self._tail的后面添加Node
            self._tail = self._tail.next  # self._tail移动到队列的最后一个位置，即维护一下self._tail
        self._size += 1  # 不论如何，入队了肯定要对self._size进行维护

    def dequeue(self):
        """
        队首元素出队，注意是在self._head处进行出队操作
        时间复杂度：O(1)
        :return: 队首元素所携带的值
        """
        if self.isEmpty():  # 判空操作
            raise Exception('Dequeue failed, please check out the size.')
        retNode = self._head  # 记录一下待出队元素，便于返回其值
        self._head = self._head.next  # self._head移动到下一个元素
        retNode.next = None  # 将retNode从队列中彻底断绝联系，使回收器能够将retNode回收

        if self.isEmpty():  # 如果队列中只有一个元素，出队后空了，需要同时对self._tail做相应的处理
            self._tail = None  # 将self._tail设为None

        self._size -= 1  # 维护self._size
        return retNode.elem  # 返回出队元素的值

    def getFront(self):
        """
        看一下队首元素的值
        时间复杂度：O(1)
        :return: 队首元素的值
        """
        return self._head.elem

    def printLinkedListQueue(self):
        """打印队列"""
        print('Queue: Head---', end='')
        cur = self._head  # 从头开始
        while cur != None:  # 只要cur不是None，就打印并且往后撸
            cur.printNode()  # 调用Node的打印函数
            cur = cur.next
        print('---Tail')
        print('Size: %d' % (self.getSize()))

if __name__ == '__main__':
    import numpy as np

    np.random.seed(7)
    test = LinkedListQueue()
    print(test.getSize())
    print(test.isEmpty())
    for i in range(15):     #入队15次
        test.enqueue(np.random.randint(10))
    test.printLinkedListQueue()
    for i in range(12):
        test.dequeue()      # 出队12次，不用返回值了
    test.printLinkedListQueue()
