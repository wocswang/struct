# -*- coding: utf-8 -*-
from maxheap import MaxHeap  # 从maxheap.py文件中导入我们上一节实现MaxHeap类
from Array import Arr # 导入我们以前实现的数组

class PriorityQueue:
    def __init__(self, initial_capacity=20):
        """
        Description: 优先队列的构造函数
        Params:
        initial_capacity: 初始容量，由于底层是我们实现的数组类，有自动扩容，所以后面的操作不用过多的考虑底层。
        """
        self._data = MaxHeap(initial_capacity)   # 初始化我们的最大堆

    def isEmpty(self):
        """
        Description: 判空
        Returns:
        bool值，空为True
        """
        return self._data.isEmpty()   # 直接调用maxHeap的isEmpty就好了

    def getSize(self):
        """
        Description: 获取当前二叉堆中有效元素的个数
        Returns:
        有效元素的个数
        """
        return self._data.getSize()   # 直接调用maxHeap的getSize

    def enqueue(self, elem):
        """
        Description: 将元素elem入队
        时间复杂度：O(logn)
        Params:
        - elem: 待入队元素
        """
        self._data.add(elem)    # 调用MaxHeap的add函数就完事了

    def getFront(self):
        """
        Description: 看一眼队首的元素是谁，也就是优先级最高的元素
        时间复杂度：O(1)
        Returns:
        队首的元素
        """
        return self._data.findMax()   # 堆顶的元素就是优先级最高的元素呀，所以调用MaxHeap的findMax就好了

    def dequeue(self):
        """
        Description: 将队首元素出队，并将其返回
        时间复杂度：O(logn)
        Returns:
        出队元素的值
        """
        return self._data.extractMax()  # 直接调用MaxHeap的extractMax，函数里面有检查了，就不需要判空了


"""基于数组的优先队列的实现，纯粹是为了对比用才实现的，主要还是要掌握基于最大堆的优先队列，这个看看就好"""
class ArrayPriorityQueue:

    def __init__(self):
        """基于我们以前实现的数组的优先队列的构造函数"""
        self._data = Arr()

    def isEmpty(self):
        """
        Description: 判空
        Returns:
        bool值，空为True
        """
        return self._data.isEmpty()      # 调用数组的isEmpty函数

    def getSize(self):
        """
        Description: 获取当前二叉堆中有效元素的个数
        Returns:
        有效元素的个数
        """
        return self._data.getSize()      # 调用数组的getSize函数

    def enqueue(self, elem):
        """
        Description: 将元素elem入队
        时间复杂度：O(1)
        Params:
        - elem: 待入队元素
        """
        self._data.addLast(elem)         # 直接插入到队尾，此时复杂度为O(1)

    def getFront(self):
        """
        Description: 看一眼队首的元素是谁，也就是优先级最高的元素
        时间复杂度:O(n)
        Returns:
        队首的元素
        """
        return self._data[self._data.get_Max_index()]   # 先获取最大值索引，再得到元素值即可

    def dequeue(self):
        """
        Description: 将队首元素出队，并将其返回
        时间复杂度：O(n)
        Returns:
        出队元素的值
        """
        return self._data.removeMax()   # 直接调用数组的removeMax函数就好


if __name__ == '__main__':
    import numpy as np

    np.random.seed(7)

    nums = 10000  # 操作数目为10000次
    max_heap_PriorityQueue = PriorityQueue()  # 基于最大堆的优先队列的对象
    arr_PriorityQueue = ArrayPriorityQueue()  # 基于数组的优先队列的对象

    record_list1 = []
    record_list2 = []


    def check_list(alist, flag):
        """
        Description: 检查输入数组是否是严格的降序排列
        Params:
        - alist: 输入的list
        - flag: bool值，判断测试的是基于最大堆的优先队列还是基于数组的优先队列
        """
        for i in range(1, len(alist) - 1):
            if alist[i] > alist[i - 1]:
                raise Exception('Error! The list is not absolutely a reversed list!')
        if flag:
            print('Priority Queue which is based on the MaxHeap test completed.')  # True为测试的基于最大堆的优先队列
        else:
            print('Priority Queue which is based on the Array test completed.')  # False为测试的基于数组的优先队列


    print('检测：')  # 既然每次都在尾部添加优先队列中最大的元素（权重最高的元素），那么list应该是严格降序排列的
    check_list(record_list1, True)  # 检测基于最大堆的优先队列
    check_list(record_list2, False)  # 检测基于数组的优先队列
