# -*- coding: utf-8 -*-

import Array

class ArrayStack:
    def __init__(self,capacity=10):
        """
        栈构造函数
        :param capacity: 栈的最大容量
        """
        self.array = Array.Arr(capacity)    # 栈的底层由我们上一节所写的Arr类来实现

    def getSize(self):
        """
        获得栈内有效元素的个数
        :return: 有效元素的个数
        """
        return self.array.getSize()     # 直接复用Arr类的getSize()方法

    def isEmpty(self):
        """
        判断栈是否为空
        :return: bool值，空为True
        """
        return self.array.isEmpty()     # 复用Arr类的isEmpty()方法


    def getCapacity(self):
        """
       这个方法是基于Arr类的特有的方法，但是一般来说用户并不需要调用这个方法。
       :return: 当前栈的最大容量
       """
        return self.array.getCapacity()     # 复用Arr类的getCapacity()方法

    def push(self,elem):
        """
       入栈操作
       tip：在这里我们将Arr数组的尾部当做栈顶，因为此时栈顶的插入与删除操作的时间复杂度都是O(1)的，因为不需要移动元素啦。
       时间复杂度：O(1)
       :param elem: 将要入栈的元素
       """
        self.array.addLast(elem)    # 复用Arr类的尾添加addLast方法

    def pop(self):
        """
        栈顶元素的出栈操作
        时间复杂度：O(1)
        :return: 出栈的元素
        """
        return self.array.removeLast()      # 复用Arr类的尾删除removeLast方法

    def peek(self):
        """
        看一眼栈顶元素是谁
        时间复杂度：O(1)
        :return: 栈顶的元素
        """
        return self.array.getLast()          # 复用Arr类的getLast方法

    def printStack(self):
        """对栈进行打印操作"""
        print('Stack:', end=' ')        # 左边为栈底
        for i in range(self.getSize()):
            if i != self.getSize() -1:
                print(self.array[i], end=' ')       # 我们实现的底层数组是支持索引功能的，得益于self.__getitem__方法，放心用- -
            else:
                print(self.array[i],end=' ')        # 为了对称，强迫症--

        print('---Top')                             # 右边为栈顶
        print('Size:', self.getSize())              # 有效元素数目


if __name__ =='__main__':
    import numpy as np
    np.random.seed(7)
    a=ArrayStack()
    print(a.getSize())
    print(a.isEmpty())
    print(a.getCapacity())
    for i in range(15):
        a.push(np.random.randint(10))
    a.printStack()
    for i in range(4):
        a.pop()     # 就不用pop函数的返回值了
    a.printStack()
    print(a.peek())