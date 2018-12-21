# -*- coding: utf-8 -*-
from Array import Arr


class MaxHeap:
    def __init__(self, capacity_=20):
        """二叉堆的构造函数"""
        self._data = Arr(capacity=capacity_)  # 调用数组的构造函数就可以了，别忘了我们的数组是支持索引操作的

    def isEmpty(self):
        """
        Description: 判空
        Returns:
        bool值，空为True
        """
        return self._data.isEmpty()  # 直接调用数组的判空函数

    def getSize(self):
        """
        Description: 获取当前二叉堆中有效元素的个数
        Returns:
        有效元素的个数
        """
        return self._data.getSize()

    def add(self, elem):
        """
        Description: 向堆中添加元素elem
        时间复杂度：O(logn)
        Params:
        - elem: 待添加元素
        """
        self._data.addLast(elem)  # 由于是一棵完全二叉树，因此直接向数组尾部添加元素就完事了，
        # 但是必须要对新添加的这个元素进行相应的维护操作，使其继续满足堆的性质。
        # 空间问题不用考虑，有自动扩容
        self._shiftUp(self.getSize() - 1)  # addLast操作中已经维护了self._size，所以此时新添加的元素位于self.getSize()-1索引处
        # 调用self._shiftUp来上移(shiftup)位于这个索引的元素，使其满足堆的性质

    def findMax(self):
        """
        Description: 看一下堆中的最大值（也就是优先级最高的元素）
        时间复杂度：O(1)
        Returns:
        优先级最高的元素的值
        """
        if self.isEmpty():
            raise Exception('Error! The maxheap is empty!')
        return self._data[0]  # 就是0索引处的元素的值

    def extractMax(self):
        """
        Description: 将堆中最大元素取出来，并返回其相应的值。
        问题：  取出后，为了维护堆的性质，由谁来代替最大值的位置呢？如果要将两个子树进行合并，非常的复杂， 我们这样来做：
                将数组中的最后一个元素放到索引0的位置，然后对索引0处的元素进行shiftDown操作，顾名思义，与shiftUp的操作是
                处于对立关系的，从而维护堆的性质
        Returns:
        堆中最大的元素的值（索引0处的元素的值）
        """
        ret = self.findMax()  # 先找到最大值，便于返回，这里不用判空了哈，findMax已经做了。
        self._data.swap(0, self.getSize() - 1)  # 将数组尾部的元素和索引0处的元素交换
        self._data.removeLast()  # 此时将数组尾部的元素删除（也就是最大值，我们已经记录过了，删除就完事了）
        self._shiftDown(0)  # 此时对新来的索引0处的元素进行shiftDown操作，从而满足堆的性质
        return ret  # 将最大值返回

    def replace(self, elem):
        """
        Description: 取出堆顶的元素，然后在添加一个元素elem，返回原先堆顶的元素。
        实现这个方法可以从我们已经实现的方法组合来实现，先extacrmax()，再add()操作，这样两侧O(logn)的操作，
        在这里我们通过一个O(logn)的方法来实现。
        时间复杂度：O(logn)
        Params:
        - elem: 待添加元素
        Returns:
        原先堆顶的元素
        """
        ret = self.findMax()  # 找到栈顶元素并用ret记录，便于返回
        self._data.set(0, elem)  # 直接将堆顶元素设为elem，调用数组的set函数，时间复杂度为O(1)
        self._shiftDown(0)  # 新设置的值极有可能破坏了堆的性质，所以将索引0处的元素进行shiftDown操作，使其最后满足堆的性质
        return ret  # 将原先堆顶元素返回

    def printMaxHeap(self):
        """对堆元素进行打印操作"""
        self._data.printArr()  # 直接调用数组的printArr()函数即可

    # private
    def _parent(self, index):
        """
        Description: 获取index索引处元素的父亲节点的index
        Params:
        - index: 传入的索引值
        Returns:
        其父亲所在的位置
        """
        if index == 0:  # 非法index，这个位置是二叉堆根节点的位置，没有父亲节点。
            raise Exception('index-0 doesn\'t have parent.')
        return (index - 1) // 2  # 根据公式返回就好了，建议画图理解下，很简单

    def _leftChild(self, index):
        """
        Description: 获取index索引处元素的左孩子节点的index
        Params:
        - index: 传入的索引值
        Returns:
        其左孩子所在的位置
        """
        return index * 2 + 1

    def _rightChild(self, index):
        """
        Description: 获取index索引处元素的右孩子节点的index
        Params:
        - index: 传入的索引值
        Returns:
        其右孩子所在的位置
        """
        return index * 2 + 2

    def _shiftUp(self, k):
        """
        Description: 对位于索引k的元素进行上移操作，移动到合适的位置，从而满足堆的性质
        Params:
        - k: 传入的索引值
        """
        while k > 0 and self._data[k] > self._data[self._parent(k)]:  # 如果k>0(没到根节点，也就是还有父亲节点)，并且索引k处的元素大于其父亲的元素
            self._data.swap(k, self._parent(k))  # 交换
            k = self._parent(k)  # k移动到父亲节点的索引处，看是否还需要上移，反正只要不到根节点就一直判断嘛，直到合适的位置

    def _shiftDown(self, k):
        """
        Description: 对位于索引k的元素进行下移操作，移动到合适的位置，从而满足堆的性质
        Params:
        - k: 传入的索引值
        """
        while (self._leftChild(k) < self.getSize()):  # 如果左孩子的索引还有效（想一想为什么不是右孩子，如果判断的是右孩子的索引值，就会少判断一种情况：
            # 就是右孩子的索引无效，但是左孩子的索引还有效）
            j = self._leftChild(k)  # 此时左孩子的索引有效，用j来标记这个索引
            if self._rightChild(k) < self.getSize():  # 还没有判断右孩子，肯定是要和两个孩子的最大值进行交换，这样在交换后才能满足堆的定义：孩子节点的值
                # 不大于父亲节点的值，所以要找到两个孩子的最大值，如果右孩子有效：
                if self._data[self._rightChild(k)] > self._data[j]:  # 看一下右孩子的值是否大于左孩子的值
                    j = self._rightChild(k)  # 如果大于，j就等于右孩子的索引，否则什么也不做
            # 此时索引j等于位于索引k处元素的两个孩子的最大值的索引
            if self._data[k] >= self._data[j]:  # 此时索引k的值已经大于两个孩子的最大值了
                break  # 直接退出循环
            self._data.swap(k, j)  # 否则就和最大值交换
            k = j  # ｋ继续往下走，看是否需要继续进行交换操作来满足最大堆的定义　

    @staticmethod
    # 独立的一个实现
    def heapify(alist):
        """
        Description: 传入一个列表，并自动对列表中的所有元素进行堆排列。实在是因为python
        没有构造函数的重载功能，我迫不得已才把这个功能单独抽出来作为一个静态函数，有一点不方便。。。
        分析： 实现这个功能很简单，新建一个空的MaxHeap，然后将列表中的所有元素一个一个的add
              到MaxHeap中，这样做时间复杂度为O(nlogn)。本函数要实现一个时间复杂度为O(n)的堆
              排列功能，至于为什么是O(n)的，我也不知道，感兴趣的可以看一下heapify的时间复杂度的
              数学推导，但是要知道O(n)与O(nlogn)之间性能是质的飞跃！
        时间复杂度：O(n)
        Params:
        - alist: 一个列表，里面的元素是要进行堆排列的全部元素
        Returns:
        一个满足堆排列（最大堆）的list，注意这个函数是in-place操作哦。
        """

        def shiftDown(alist, index):
            """
            Description: 和MaxHeap的self._shiftDown操作是一样，只不过我需要在这里再实现一个，才
            可以调用--!
            Params:
            - alist: 一个列表
            - index: 要shiftDown的索引
            """
            length = len(alist)  # 就不详细讲解了，跟前面的self._shiftDown是一样的～
            while index * 2 + 1 < length:
                j = index * 2 + 1
                if j + 1 < length:
                    if alist[j + 1] > alist[j]:
                        j += 1
                if alist[index] >= alist[j]:
                    break
                alist[index], alist[j] = alist[j], alist[index]
                index = j

        length = len(alist)
        # 这里要记住堆有一个极其重要的性质～就是堆的第一个非叶子节点的索引一定是
        # ((length - 1) - 1) // 2
        # 其实想一想也很简单，length - 1这个索引一定是数组的最后一个元素，最后一个元素的父亲
        # 节点的索引一定是第一个非叶子节点的索引呀，即parent(length - 1)，这里并没有parent函数
        # 所以展开就是 ((length - 1) - 1) // 2
        # 从第一个非叶子节点开始，一直到索引0处（二叉堆根的索引），都执行shiftDown操作，最后
        # 这个数组也就变成了一个堆。为什么不用管  (((length - 1) - 1) // 2, length - 1]左
        # 开右闭区间内的点呢？原因也很简单，在非叶子节点shiftDown的过程中自动就将这些点维护了！
        for i in range(((length - 1) - 1) // 2, -1, -1):  # 遍历第一个非叶子节点开始一直到根节点
            shiftDown(alist, i)  # 都shiftDown一次就完事了
        return alist




if __name__ =='__main__':
    import numpy as np

    np.random.seed(7)

    test_maxheap = MaxHeap()
    nums = 100000  # 操作数

    for i in range(nums - 1):
        test_maxheap.add(np.random.randint(1000))  # 99999次添加随机数操作
    test_maxheap.add(6666)  # 再添加一个最大的，便于验证

    print('添加元素操作后的Size：', test_maxheap.getSize())
    print('此时堆中最大值：', test_maxheap.findMax())

    record = []
    for i in range(nums):
        record.append(test_maxheap.extractMax())  # 100000次提取最大元素操作并append到record中
        # 不出意外，record中的元素应该是完全降序排列的

    for i in range(1, len(record)):  # 测试record是否真的是降序排列
        if record[i - 1] < record[i]:
            raise Exception('Error, the list is not absolutely a reversed list.')
    print('Test MaxHeap completed.')

    print('将元素全部抽取后是否为空堆？', test_maxheap.isEmpty())

    print('---------------------------------------------')
    print('新建一个堆完成replace的测试，10次添加操作后：')


    test_maxheap2 = MaxHeap()
    for i in range(10):
        test_maxheap2.add(i)
    test_maxheap2.printMaxHeap()
    print('抽取堆顶元素并添加一个0.7：')  # 0.7这里选的不好，因为浮点数一旦涉及到判等操作会出现问题，但是字在这里没有判等操作
    test_maxheap2.replace(0.7)
    test_maxheap2.printMaxHeap()

    print('测试heapify函数')
    test_list = [i for i in range(30)]
    print('待堆排列的元素：', test_list)
    print('堆排列后：')
    print(MaxHeap.heapify(test_list))  # 可以动手画一下是满足堆排列性质的。




