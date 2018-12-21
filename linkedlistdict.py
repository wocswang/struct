# -*- coding: utf-8 -*-
class Node:
    def __init__(self, key=None, value=None, next=None):
        """
        Description: 节点的构造函数
        Params:
        - key: 传入的键值，默认为None
        - value: 传入的键所对应的value值，默认为None
        - next: 指向下一个Node的标签，默认为None
        """
        self.key = key
        self.value= value
        self.next = next     # 下一个节点为None

class LinkedListDict:
    """以链表作为底层数据结构的字典类"""
    def __init__(self):
        """
        Description: 字典的构造函数
        """
        self._dummyhead = Node()        # 建立一个虚拟头结点，前面讲过，不再赘述
        self._size = 0              # 字典中有效元素的个数


    def getSize(self):
        """
        Description: 获取字典中有效元素的个数
        Returns:
        有效元素的个数
        """
        return self._size

    def isEmpty(self):
        """
        Description: 判断字典是否为空
        Returns:
        bool值，空为True
        """
        return self._size == 0

    def contains(self, key):
        """
        Description: 查看字典的键中是否包含key
        时间复杂度：O(n)
        Params:
        - key: 待查询的键值
        Returns:
        bool值，存在为True
        """
        return self._getNode(key) is not None   # 调用self._getNode私有函数，看返回值是否是None

    def get(self, key):
        """
        Description: 得到字典中键为key的value值
        时间复杂度：O(n)
        Params:
        - key: 待查询的键值
        Returns:
        相应的value值。若key不存在，就返回None
        """
        node = self._getNode(key)        # 拿到键为key的Node
        if node:                        # 如果该Node不是None
            return node.value           # 返回对应的value
        else:
            return None                 # 否则（此时不存在携带key的Node）返回None


    def add(self, key, value):
        """
       Description: 向字典中添加key，value键值对。若字典中已经存在相同的key，更新其value，否咋在头部添加Node，因为时间复杂度为O(1)
       时间复杂度：O(n)
       Params:
       - key: 待添加的键值
       - value: 待添加的键值的value
       """
        node = self._getNode(key)   # 先判断字典中是否存在这个键
        if node != None:             # 已经存在
            node.value = value           # 更新这个Node的value

        else:
            self._dummyhead.next = Node(key, value, self._dummyhead.next)           # 否则在头部添加，添加操作链表那一章有讲，这里不再赘述
            self._size +=1      # 维护self._size

    def set(self,key,new_value):
        """
       Description: 将字典中键为key的Node的value设为new_value。注意，为防止与add函数发生混淆，
       此函数默认用户已经确信key在字典中，否则报错。并不会有什么新建Node的操作，因为这么做为与add函数有相同的功能，就没有意义了。
       时间复杂度：O(n)
       Params:
       - key: 将要被设定的Node的键
       - new_value: 新的value值
       """
        node = self._getNode(key)   # 找到携带这个key的Node
        if node is None:         # 没找到
            raise Exception('%s doesn\'t exist!' % key)  # 报错就完事了
        node.value= new_value            # 找到了就直接将返回节点的value设为new_value

    def remove(self,key):
        """
       Description: 将字典中键为key的Node删除。注：若不存在携带key的Node，返回Node就好。
       时间复杂度：O(n)
       Params:
       - key: 待删除的键
       Returns:
       被删除节点的value
       """
        pre = self._dummyhead       # 找到要被删除节点的前一个节点（惯用手法，不再赘述）
        while pre.next is not None:         # pre的next只要不为空
            if pre.next.key == key:         # 如果找到了
                break                       # 直接break，此时pre停留在要被删除节点的前一个节点
            pre = pre.next                  # 否则往后撸

        if pre.next is not None:        # 此时找到了
            delNode = pre.next              # 记录一下要被删除的节点，方便返回其value
            pre.next = delNode.next         # 不再赘述，如果不懂就去看看链表那节吧。O(∩_∩)O
            delNode.next = None             # delNode的下一个节点设为None，使delNode完全与字典脱离，便于垃圾回收器回收
            self._size -=1                  # 维护self._size
            return delNode.value             # 返回被删除节点的value

        return None                 # 此时pre的next是None!说明并没有找到这个key，返回None就好了。

    def printLinkedListDict(self):
        """打印字典元素"""
        cur = self._dummyhead.next
        while cur != None:
            print('[Key: %s, Value: %s]' % (cur.key, cur.value), end='-->')
            cur = cur.next
        print('None')

    # private functions
    def _getNode(self, key):
        """
       Description: 一个辅助函数，是私有函数。功能就是返回要查找的键的Node，若key不存在就返回None
       时间复杂度：O(n)
       Params:
       - key: 要查找的键值
       Returns:
       返回带查找key的节点，若不存在返回None
       """
        cur = self._dummyhead.next               # 记录当前节点
        while cur != None:                      # cur没到头
            if cur.key == key:                   # 找到了
                return cur                      # 返回当前的Node
            cur = cur.next                      # 没找到就往后撸
        return None                             # cur此时为None了。。说明已经到头还没找到，返回None



if __name__ == '__main__':
    test_map = LinkedListDict()
    print('初始字典Size：', test_map.getSize())
    print('初始字典是否为空：', test_map.isEmpty())
    for i in range(10):
        test_map.add(i,str(i) +'_index')
    print('10次添加操作后：')
    print('Size: ', test_map.getSize())
    print('是否包含7？', test_map.contains(7))
    test_map.printLinkedListDict()  # 由于在头部插入，所以打印是反向的哦～
    print('键为6的value：', test_map.get(6))
    print('将键值为4的value设为 "你好呀",并打印：')
    test_map.set(4, '你好呀')
    test_map.printLinkedListDict()
    print('删除键为7的元素，并打印：')
    test_map.remove(7)
    test_map.printLinkedListDict()
    print('此时的Size为：', test_map.getSize())