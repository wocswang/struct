# -*- coding: utf-8 -*-

from loopqueue import LoopQueue

class Node:
    def __init__(self, key=None, value=None):
        """
        Description: 节点类的构造函数
        """
        self.key = key       # 键
        self.value = value   # value
        self.left = None    # 指向左孩子的标签
        self.right=None      # 指向右孩子的标签

class BstDict:
    def __init__(self):
        """
       Description: 基于二分搜索树的字典类的构造函数
       """
        self._root = None       # 初始化根节点为None
        self._size = 0          # 初始化self._size

    def getSize(self):
        """
        Description: 获取字典内有效元素的个数
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


    def add(self, key, value):
        """
               Description: 向字典中添加键-值对，若键已经存在字典中，那就更新这个键所对应的value
               时间复杂度：O(logn)
               Params:
               - key: 待添加的键
               -value: 待添加的键所对应的value
               """
        self._root = self._add(self._root, key,value)       # 调用self._add方法，常规套路

    def contains(self, key):
        """
               Description: 查看字典的键中是否包含key
               时间复杂度：O(logn)
               Params:
               - key: 待查询的键值
               Returns:
               bool值，存在为True
               """
        return self._getNode(self._root,key) is not None        # 调用self._getNode私有函数，看返回值是否是None

    def get(self, key):
        """
                Description: 得到字典中键为key的value值
                时间复杂度：O(logn)
                Params:
                - key: 待查询的键值
                Returns:
                相应的value值。若key不存在，就返回None
                """
        node = self._getNode(self._root,key)
        if node:
            return node.value
        else:
            return None          # 否则（此时不存在携带key的Node）返回None



    def set(self,key,new_value):
        """
       Description: 将字典中键为key的Node的value设为new_value。注意，为防止与add函数发生混淆，
       此函数默认用户已经确信key在字典中，否则报错。并不会有什么新建Node的操作，因为这么做为与add函数有相同的功能，就没有意义了。
       时间复杂度：O(logn)
       Params:
       - key: 将要被设定的Node的键
       - new_value: 新的value值
       """
        node = self._getNode(self._root,key)
        if node is None:
            raise Exception('%s doesn\'t exist!' % key)   #报错就完事了
        node.value = new_value

    def remove(self,key):
        """
                Description: 将字典中键为key的Node删除。注：若不存在携带key的Node，返回Node就好。这个remove函数和前面的二分搜索树的remove函数极为相似，不理解的可以去前面看一下
                时间复杂度：O(logn)
                Params:
                - key: 待删除的键
                Returns:
                被删除节点的value
                """
        ret = self._minimum(self._root)         # 调用self._minimum函数保存携带最小值的节点，便于返回
        self._root = self._remove(self._root,key)       # 调用self._remove函数
        return ret.value                    # 返回携带最小值节点的value

    def printBstDict(self):
        """对字典进行打印操作，这里使用广度优先遍历，因为比较直观"""
        if self._root is None:
            return
        queue = LoopQueue()
        queue.enqueue(self._root)
        while not queue.isEmpty():
            node = queue.dequeue()
            print('[Key: %s, Value: %s]' % (node.key, node.value))
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)


    # private method
    def _add(self, node, key, value):
        """
        Description: 向以node为根的二叉搜索树中添加键-值对
        Params:
        - node: 根节点
        - key: 待添加的键
        -value: 待添加的键所对应的value
        Returns:
        添加后新的根节点
        """
        getNode = self._getNode(self._root, key)        # 先判断字典中是否存在携带这个键的Node
        if getNode is not None:     # 如果已经存在
            getNode.value= value        # 将这个节点的value设为新传入的value就好
            return node              # 返回根节点，不需要维护self._size哦

        if node is None:            # 递归到底的情况，该添加节点啦
            self._size +=1              # 维护self._size
            return Node(key,value)       # 将新节点返回

        if key < node.key:           # 待添加key小于node的key，向左子树继续前进。这里的操作在二叉搜索树中详细讲过，就不BB了
            node.left = self._add(node.left, key, value)
        elif key > node.key:        # 待添加key大于node的key，向右子树继续前进。
            node.right = self._add(node.right,key,value)
        return node              # 将node返回，这样在递归的回归过程中逐级返回，最终返回的是根节点

    def _remove(self,node,key):
        """
                Description: 将以node为根节点的字典中键为key的Node删除。注：若不存在携带key的Node，返回Node就好。
                时间复杂度：O(logn)
                Params:
                - node: 以node为根节点的字典
                - key: 待删除的节点所携带的键
                Returns:
                删除操作后的根节点
                """
        if node is None:    # 到头了都没找到key
            return None     # 直接返回None

        if key < node.key:      # 待删除key小于当前Node的key
            node.left = self._remove(node.left,key)     # 往左子树递归
            return node
        elif node.key <key:     # 待删除key大于当前Node的key
            node.right = self._remove(node.right, key)      # 往右子树递归
            return node
        else:                                # 此时待删除key和当前Node的key相等，别忘了有三种情况
            if node.left is None:            # 左子树为空的情况
                right_node = node.right         # 记录当前Node的右孩子
                node.right =None                 # 当前Node的右孩子设为None，便于垃圾回收
                self._size -=1                  # 维护self._size
                return right_node                # 将被删除Node的右孩子返回，即用右孩子来代替被删除节点的位置

            elif node.right is None:         # 右子树为空的情况，大同小异，不再赘述
                left_node =node.left
                node.left = None
                self._size -=1
                return left_node
            else:       # 这里不再赘述了，不清楚的话回去看看二分搜索树那章，一样的操作
                successor = self._minimum(node.right)
                successor.right = self._removeMin(node.right)
                self._size +=1
                successor.left = node.left
                node.left = node.right = None
                self._size -=1
                return successor

    def _minimum(self, node):
        """
                Description: 返回以node为根的二分搜索树的携带最小值的节点，下面的这些操作在二分搜索树中均有涉及，如果看不懂回到那一章再理解下就好了
                Params:
                - node: 根节点
                Returns:
                携带最小值的节点
                """
        if node.left is None:       # 递归到底的情况，node的左孩子已经为空了
            return node              # 返回node

        return self._minimum(node.left)      # 否则往左子树继续撸

    def _removeMin(self,node):
        """
               Description: 删除以node为根的二分搜索树的携带最小值的节点，同理，返回删除后的根节点
               Params:
               - node: 根节点
               Returns:
               返回删除操作后的树的根节点
               """
        if node.left is None:       # 递归到底的情况，node的左孩子已经为空
            right_node = node.right     # 记录node的右孩子，为None也无所谓的
            node.right = None           # 将node的右孩子设为None，使其与树断绝联系，从而被垃圾回收
            self._size -=1              # 维护self._size
            return right_node            # 返回node的右孩子，即用右孩子来代替当前的node


    def _getNode(self, node, key):
        """
        Description: 设置一个根据key来找到以node为根的二叉搜索树的相对应的Node的私有函数，便于方便的实现其他函数
        Params:
        - node: 传入的根节点
        - key: 带查找的key
        Returns:
        携带key的节点Node, 若不存在携带key的节点，返回None
        """
        if node is None:        # 都到底了还没有找到，直接返回None
            return None

            # 注意我们的二分搜索树依旧不包含重复的键哦～这也是字典的基本特点
        if key <node.key:        # 待查找的key小于当前节点的key，向左子树递归就完事了
            return self._getNode(node.left, key)
        elif node.key < key:        # 待查找的key大于当前节点的key，向右子树递归就完事了
            return self._getNode(node.right,key)
        else:                       # 此时带查找的key和node.key是相等的，直接返回这个Node就好
            return node



if __name__ == '__main__':
    test_bst =BstDict()
    print('初始Size: ', test_bst.getSize())
    print('是否为空？', test_bst.isEmpty())

    add_list = [15, 4, 25, 22, 3, 19, 23, 7, 28, 24]
    print('待添加元素：', add_list)
    for add_elem in add_list:
        test_bst.add(add_elem, str(add_elem) + 'x')

    print('添加元素后打印集合：')
    test_bst.printBstDict()
    print('此时的Size: ', test_bst.getSize())
    print('字典中是否包含键23？', test_bst.contains(23))
    print('获取键23的value：', test_bst.get(23))
    print('将键为7的value设为"努力学习"并打印：')
    test_bst.set(7, '努力学习')
    test_bst.printBstDict()
    print('删除键22并打印：')
    test_bst.remove(22)
    test_bst.printBstDict()
    print('此时的Size：', test_bst.getSize())


