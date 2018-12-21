# -*- coding: utf-8 -*-

from bst import BST

class BstSet:
    def __init__(self):
        """用二分搜索树作为底层实现的集合的构造函数"""
        self._data = BST()       # 一个空的二分搜索树

    def getSize(self):
        """
        Description: 返回集合的大小
        Retures:
        集合大小
        """
        return self._data.getSize()     # 直接调用二分搜索树的getSize方法

    def isEmpty(self):
        """
        Description: 判断集合是否为空
        Returns:
        bool值，空为True
        """
        return self._data.isEmpty()     # 直接调用二分搜索树的isEmpty方法

    def add(self, elem):
        """
        Description: 向集合中添加元素elem，时间复杂度：O(logn)
        Params:
        - elem: 待添加的元素
        """
        self._data.add(elem)        # 直接调用二分搜索树的add方法，注意我们实现的二分搜索树是不包含重复元素的哦，满足集合的概念。不清楚的话回去看一下二分搜索树的add方法就好了

    def contains(self, elem):
        """
        Description: 查询集合中是否存在元素elem，时间复杂度：O(logn)
        Params:
        - elem: 待查询元素
        Returns:
        bool值，存在为True
        """
        return self._data.contains(elem)        # 直接调用二分搜索树的contains方法

    def remove(self, elem):
        """
       Description: 将elem从集合中删除，注意若elem不存在，我们什么也不做。时间复杂度：O(logn)
       Params:
       - elem: 待删除元素
       """
        self._data.remove(elem)      # 直接调用二分搜索树的remove方法

    def printSet(self):
        """
       Description: 打印集合，这里采用中序遍历的方法来打印集合元素。随便选啦，前中后以及层序都可以的。
       """
        self._data.inOrder()        # 直接调用二分搜索树的inOrder方法，这样打印出来的元素是从小到达排列的！


if __name__ =='__main__':
    import numpy as np
    np.random.seed(7)

    test_set =BstSet()
    print('初始化时是否为空？', test_set.isEmpty())
    for i in range(10):  # 10次添加操作
        test_set.add(np.random.randint(100))
    print('10次添加操作后集合元素为：')
    test_set.printSet()
    print('Size: ', test_set.getSize())
    print('此时集合中是否含有元素47？', test_set.contains(47))
    print('-----------------------------------------------------')
    print('添加一个重复元素47后，集合所包含的全部元素以及集合大小为：')
    test_set.add(47)
    test_set.printSet()
    print()
    print('Size: ', test_set.getSize())
    print('-----------------------------------------------------')
    print('删除元素47后，集合所包含的全部元素以及集合大小为：')
    test_set.remove(47)
    test_set.printSet()
    print()
    print('Size: ', test_set.getSize())
    print('-----------------------------------------------------')