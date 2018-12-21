# -*- coding: utf-8 -*-


class Node:
    def __init__(self, elem_=None, next_=None):
        """
        节点类构造函数
        :param elem_: 节点所带的元素，默认为None
        :param next_: 指向下一个节点的标签（在python中叫做标签）
        """
        self.elem = elem_
        self.next = next_  # 都是共有的

    def printNode(self):
        """打印Node"""
        print(self.elem, end='  ')  # 就打印一下元素的值


class LinkedList:
    def __init__(self):
        """
        链表构造函数
        """
        self._dummyhead = Node()        # 虚拟头结点，作用巨大，把他当成不属于链表的哨兵节点就好
        # 如果没有dummyhead，在链表头部插入与删除操作将要特殊对待，因为找不到待操作节点的前一个节点
        # 而有了虚拟头结点后，就不存在这种情况了
        self._size = 0       # 容量

    def getSize(self):
        """
        获得链表中节点的个数
        :return: 节点个数
        """
        return self._size

    def isEmpty(self):
        """
        判断链表是否为空
        :return: bool值，空为True
        """
        return self.getSize() == 0

    def add(self, index, elem):
        """
        普适性的插入功能
        时间复杂度：O(n)
        :param index: 要插入的位置（注意index对于用户来说也是从零开始的，这里我没做更改）
        :param elem: 待插入的元素
        """
        if index < 0 or index > self._size:     # 有效性检查
            raise Exception('Add failed. Illegal index')
        prev = self._dummyhead      # 从虚拟头结点开始，注意虚拟头结点不属于链表内的节点，当做哨兵节点来看就好了
        for i in range(index):      # 往后撸，直到待操作节点的前一个节点
            prev = prev.next
        prev.next = Node(elem, prev.next)
        # 先看等式右边，创建了一个节点对象，携带的元素是elem，指向的元素就是index处的节点，即
        # 现在有一个新的节点指向了index处的节点
        # 并将它赋给index节点处的前一个节点的next，是的prev的下一个节点就是这个新节点，完成拼接操作
        # 可以分解成三句话：  temp = Node(elem); temp.next = prev.next; prev.next = temp
        # 画个图就很好理解啦
        self._size += 1 # 维护self._size

    def addFirst(self, elem):
        """
        将elem插入到链表头部
        时间复杂度：O(1)
        :param elem: 要插入的元素
        """
        self.add(0, elem)       # 直接点用self.add

    def addLast(self, elem):
        """
        链表尾部插入元素elem
        时间复杂度：O(n)
        :param elem: 待插入的元素
        """
        self.add(self._size, elem)      # 调用self.add

    def remove(self, index):
        """
        删除第index位置的节点
        时间复杂度：O(n)
        :param index: 相应的位置，注意从零开始
        :return: 被删除节点的elem成员变量
        """
        if index < 0 or index >= self.getSize():    # index合法性检查
            raise Exception('Remove falied. Illegal index')
        pre = self._dummyhead       # 同样的，要找到待删除的前一个节点，所以从dummyhead开始
        for i in range(index):      # 往后撸index个节点
            pre = pre.next
        retNode = pre.next          # 此时到达待删除节点的前一个节点，并用retNode对待删除节点进行标记，方便返回elem
        pre.next = retNode.next     # pre的next直接跨过待删除节点直接指向待删除节点的next，画个图就很好理解了
        retNode.next = None         # 待删除节点的next设为None，让它完全从链表中脱离，使得其被自动回收
        self._size -= 1             # 维护self._size
        return retNode.elem         # 返回被删除节点的elem成员变量

    def removeFirst(self):
        """
        删除第一个节点(index=0)
        时间复杂度：O(1)
        :return: 第一个节点的elem成员变量
        """
        return self.remove(0)   # 直接调用self.add方法

    def removeLast(self):
        """
        删除最后一个节点(index=self._size-1)
        时间复杂度：O(n)
        :return: 最后一个节点的elem成员变量
        """
        return self.remove(self.getSize() - 1)

    def removeElement(self, elem):
        """
        删除链表的指定元素elem，这个方法实现的是将链表中为elem的Node全部删除哦，与数组只删除最左边的第一个是不一样的！如果elem不存在我们什么也不做
        :param elem: 待删除的元素elem
        时间复杂度：O(n)
        """
        pre = self._dummyhead             # 老方法，被删除元素的前一个记为pre
        while pre.next:                   # 只要pre的next不为空
            if pre.next.elem == elem:     # pre的next的elem和elem相等
                delNode = pre.next        # 记下pre的next的节点，准备略过它
                pre.next = delNode.next   # 略过pre.next直接将pre.next置为pre.next.next
                delNode.next = None       # delNode的next置为空，被当成垃圾回收
                self._size -= 1           # 维护self._size
                # 注意此时不要pre = pre.next，因为这时候pre的next又是一个新的元素！也需要进行判断的，所以删除的是所有携带值为elem的节点
            else:
                pre = pre.next            # 不相等就往后撸就完事了


    def get(self, index):
        """
        获得链表第index位置的值
        时间复杂度：O(n)
        :param index: 可以理解成索引，但并不是索引！
        :return: 第index位置的值
        """
        if index < 0 or index >= self.getSize():    # 合法性检查
            raise Exception('Get failed.index is Valid, index require 0<=index<=self._size-1')
        cur = self._dummyhead.next      # 初始化为第一个有效节点
        for i in range(index):          # 执行index次
            cur = cur.next              # 往后撸，一直到第index位置
        return cur.elem

    def getFirst(self):
        """
        获取链表第一个节点的值
        时间复杂度：O(1)
        :return: 第一个节点的elem
        """
        return self.get(0)      # 调用self.add方法

    def getLast(self):
        """
        获取链表最后一个节点的值
        时间复杂度：O(n)
        :return: 最后一个节点的elem
        """
        return self.get(self.getSize() - 1)

    def set(self, index, e):
        """
        把链表中第index位置的节点的elem设置成e
        时间复杂度：O(n)
        :param index: 链表中要操作的节点的位置
        :param e:  将要设为的值
        """
        if index < 0 or index >= self.getSize():        # 合法性检查
            raise Exception('Set failed.index is Valid, index require 0<=index<=self._size-1')
        cur = self._dummyhead.next  # 从第一个元素开始，也就是dummyhead的下一个节点
        for i in range(index):      # 往后撸，直到要操作的节点的位置
            cur = cur.next
        cur.elem = e        # 设置成e即可

    def contains(self, e):
        """
        判断链表的节点的elem中是否存在e
        时间复杂度：O(n)
        由于并不存在索引，所以只能从头开始找，一直找。。。如果到尾还没找到就是不存在
        :param e: 要判断的值
        :return: bool值，存在为True
        """
        cur = self._dummyhead.next  # 将cur设置成第一个节点
        while cur != None:      # 只要cur有效，注意这个链表的最后一个节点一定是None，因为dummyhead初始化时next就是None，这个
            # 通过链表的这些方法只会往后移动，一直处于最末尾
            if cur.elem == e:   # 如果相等就返回True
                return True
            cur = cur.next      # 否则就往后撸
        return False            # 到头了还没找到就返回False

    def printLinkedList(self):
        """对链表进行打印操作"""
        cur = self._dummyhead.next
        print('表头：', end=' ')
        while cur != None:
            cur.printNode()
            cur = cur.next
        print('\nSize:  %d' % self.getSize())


if __name__ == '__main__':

    import numpy as np
    np.random.seed(7)

    test = LinkedList()
    print(test.getSize())
    print(test.isEmpty())
    test.addFirst(6)
    for i in range(13):
        test.addLast(np.random.randint(11))

    test.printLinkedList()
    test.add(10, 'annihilation7')
    test.printLinkedList()
    print(test.getSize())
    print(test.get(2))
    print(test.getLast())
    print(test.getFirst())
    test.set(0,30)
    test.printLinkedList()
    print(test.contains(13))
    print(test.remove(8))
    test.printLinkedList()
    print(test.removeFirst())
    test.printLinkedList()
    print(test.removeLast())
    test.printLinkedList()
    print('删除全部为7的元素：')
    test.removeElement(7)
    test.printLinkedList()
    print(test.getSize())








