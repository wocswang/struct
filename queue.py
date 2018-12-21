# -*- coding: utf-8 -*-
import Array

class Queue:
    def __init__(self, capacity=10):
        """
       构造函数
       :param capacity: 初始容量，默认值为10
       """
        self.array=Array.Arr(capacity)         # 底层由我们在第一章完成的Arr类来实现，毕竟Queue的操作只是Arr类的部分操作

    def getSize(self):
        """
        得到队列内有效元素的个数
        时间复杂度：O(1)
        :return: 有效元素的个数
        """
        return self.array.getSize()              # 复用Arr类的getSize方法，Arr类中已经对它的_size进行类很好的维护操作

    def getCapacity(self):
        """
       因为是由我们自己实现的数组作为底层数据结构，因此能够查看当前队列的容量大小，实际上这个函数用户并用不到
       时间复杂度：O(1)
       :return: 队列的容量
       """
        return self.array.getCapacity()          # 复用Arr类的getCapacity方法

    def isEmpty(self):
        """
        判断队列是否为空
        时间复杂度：O(1)
        :return: bool值，空为True
        """
        return self.array.isEmpty()             # 复用Arr类的isEmpty()方法

    def enqueue(self,elem):
        """
        入队操作，注意本文中数组右侧为队尾，左侧（索引为0的地方）为队首
        时间复杂度：O(1)
        :param elem: 将要入队的元素
        """
        self.array.addLast(elem)                # 复用Arr类的addLast操作，进行入队

    def dequeue(self):
        """
        出队操作,数组左边出队，就是在索引为0的地方出队。
        时间复杂度：O(n)
        :return: 出队的元素的值
        """
        return self.array.removeFirst()


    def getFront(self):
        """
        拿到对首的元素，因为往往队首的元素是我们关心的元素。
        时间复杂度：O(1)
        :return: 队首元素
        """
        return self.array.getFirst()            # 复用Arr类的getFirst操作，也不用进行判空神马的类，因为Arr类中的函数都帮我们干了

    def printQueue(self):
        """打印队列的操作"""
        print('Queue: Front--- ', end='')  # 左边是队首
        for i in range(self.getSize()):
            if i != self.getSize() -1:      # 强迫症。。为了打印美观- -
                print(self.array[i], end=' ')       # 别忘了我们的Arr是支持索引操作的哦
            else:
                print(self.array[i], end='')

        print(' ---Tail')  # 右边是队尾哦
        print('Size: %d' % (self.getSize()))  # 有效元素个数的打印



if __name__=='__main__':
    import numpy as np

    np.random.seed(7)
    test = Queue()
    print(test.getSize())
    print(test.getCapacity())
    print(test.isEmpty())
    for i in range(17):
        test.enqueue(np.random.randint(10))
    test.printQueue()
    for i in range(7):
        test.dequeue()
    test.printQueue()
    print(test.getFront())

