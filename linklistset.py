# -*- coding: utf-8 -*-
from linkedlist import LinkedList

class LinkedListSet:
    def __init__(self):
        """用链表作为底层数据结构实现的集合的构造函数"""
        self._data = LinkedList()   # 空链表

    def getSize(self):
        """
        Description: 返回集合的大小
        Retures:
        集合大小
        """
        return self._data.getSize()  # 调用链表的getSize方法

    def isEmpty(self):
        """
        Description: 判断集合是否为空
        Returns:
        bool值，空为True
        """
        return self._data.isEmpty()

    def add(self, elem):
        """
        Description: 向集合中添加元素elem，时间复杂度：O(n)
        Params:
        - elem: 待添加的元素
        """
        if not self._data.contains(elem):  # 注意以前实现的链表类是可以包含重复元素的，所以在这里要做一个判断，这步的时间复杂度是O(n)的
            self._data.addFirst(elem)      # 在链表头部添加元素，因为时间复杂度是O(1)的！

    def contains(self, elem):
        """
        Description: 查询集合中是否存在元素elem，时间复杂度：O(n)
        Params:
        - elem: 待查询元素
        Returns:
        bool值
        """
        return self._data.contains(elem)  # 直接调用链表的contains方法

    def remove(self, elem):
        """
        Description: 将elem从集合中删除，注意若elem不存在，我们什么也不做。时间复杂度：O(n)
        Params:
        - elem: 待删除元素
        """
        self._data.removeElement(elem)  # 直接调用链表的remove方法

    def printSet(self):
        """
        Description: 打印集合，这里采用中序遍历的方法来打印集合元素。随便选啦，前中后以及层序都可以的。
        """
        self._data.printLinkedList()  # 直接调用链表的printLinkedList方法。




if __name__ =='__main__':
    import numpy as np
    np.random.seed(7)

    test_set = LinkedListSet()
    print('初始化时是否为空？', test_set.isEmpty())
    for i in range(10):
        test_set.add(np.random.randint(100))
    print('10次添加操作后集合元素为：')
    test_set.printSet()
    print('此时集合中是否含有元素47？', test_set.contains(47))
    print('-----------------------------------------------------')
    print('添加一个重复元素47后，集合所包含的全部元素以及集合大小为：')
    test_set.add(47)
    test_set.printSet()
    print('-----------------------------------------------------')
    print('删除元素47后，集合所包含的全部元素以及集合大小为：')
    test_set.remove(47)
    test_set.printSet()
    print('-----------------------------------------------------')
