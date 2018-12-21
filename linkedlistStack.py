# -*- coding: utf-8 -*-
import linkedlist

class LinkedListStack:
    def __init__(self):
        self.stack = linkedlist.LinkedList()        # 初始化一个链表就好
        # 这时就不需要self._capacity了，因为并不需要扩容/缩容神马的

    def getSize(self):
        """
        获得栈内有效元素的个数
        :return: 有效元素的个数
        """
        return self.stack.getSize()     # 直接调用链表的getSize方法

    def isEmpty(self):
        """
        判断栈是否为空
        :return: bool值，空为True
        """
        return self.stack.isEmpty()     # 调用链表的isEmpty方法


    def push(self, elem):
        """
        入栈操作
        tip：在这里我们将链表的表头当做栈顶，因为此时栈顶的入栈与出栈操作的时间复杂度都是O(1)的
        时间复杂度：O(1)
        :param elem: 将要入栈的元素
        """
        return self.stack.addFirst(elem)    # 调用链表的addFirst方法

    def pop(self):
        """
        栈顶元素的出栈操作，同理，也在表头进行出栈操作
        时间复杂度：O(1)
        :return: 出栈的元素
        """
        return self.stack.removeFirst()      # 调用链表的removeFirst方法

    def peek(self):
        """
        看一眼栈顶元素是谁
        时间复杂度：O(1)
        :return: 栈顶的元素
        """
        return self.stack.getFirst()            # 调用链表的getFirst方法

    def printLinkListStack(self):
        """对链表栈进行打印操作"""
        print('Stack: Top--- ', end=' ')  # 左边为栈顶
        cur = self.stack._dummyhead.next
        while cur != None:
            cur.printNode()
            cur = cur.next
        print('---bottom')  # 右边为栈底
        print('Size: ', self.getSize())  # 有效元素数目


if __name__ =='__main__':
    import numpy as np

    np.random.seed(7)
    a=LinkedListStack()
    print(a.getSize())
    print(a.isEmpty())
    for i in range(15):     # 入栈15次
        a.push(np.random.randint(10))    # 就不用pop函数的返回值了
    a.printLinkListStack()
    for i in range(4):
        a.pop()
    a.printLinkListStack()
    print(a.peek())

