# -*- coding: utf-8 -*-

from arrayStack import ArrayStack
from loopqueue import LoopQueue

class Node:
    def __init__(self, elem):
        """
        节点构造函数，三个成员：携带的元素，指向左孩子的指针（标签），指向右孩子的指针（标签）
        :param elem: 携带的元素
        """
        self.elem = elem
        self.left = None        # 左孩子设为空
        self.right = None       # 右孩子设为空


class BST:
    def __init__(self):
        """
        二分搜索树的构造函数——————空树
        """
        self._root = None       # 根节点设为None
        self._size = 0          # 有效元素个数初始化为0

    def getSize(self):
        """
        返回节点个数
        :return: 节点个数
        """
        return self._size

    def isEmpty(self):
        """
        判断二分搜索树是否为空
        :return: bool值，空为True
        """
        return self._size == 0

    def add(self, elem):
        """
        向二分搜索树插入元素elem
        时间复杂度：O(logn)
        :param elem: 待插入的元素
        :return: 二分搜索树的根
        """
        self._root = self._add(self._root, elem)  # 调用私有函数self._add

    def contains(self, elem):
        """
        查看二分搜索树中是否包含elem
        时间复杂度：O(logn)
        :param elem: 待查询元素
        :return:     bool值，查到为True
        """
        return self._contains(self._root, elem)   # 调用私有函数self._contains

    def preOrfer(self):
        """
        二分搜索树的前序遍历
        时间复杂度：O(n)
        前序遍历、中序遍历以及后续遍历是针对当前的根节点来说的。前序就是把对根节点的操作放在遍历左、右子树的前面，相应的中序遍历以及后序遍历以此类推
        前序遍历是最自然也是最常用的二叉搜索树的遍历方式
        """
        self._preOrder(self._root)        # 调用self._preOrder函数

    def inOrder(self):
        """
        二分搜索树的中序遍历
        时间复杂度：O(n)
        特点：输出的元素是从小到大排列的，因为先处理左子树，到底后再处理当前节点，最后再处理右子树，而左子树的值都比当前节点小，
              右子树的值都比当前节点大，所以是排序输出
        """
        self._inOrder(self._root)         # 调用self._inOrder函数

    def postOrder(self):
        """
        二分搜索树的后序遍历
        应用场景：二叉搜索树的内存回收，例如C++中的析构函数
        时间复杂度：O(n)
        """
        self._postOrder(self._root)       # 调用self._postOrder函数

    def preOrderNR(self):
        """
        前序遍历的非递归写法
        此时需要借助一个辅助的数据结构————栈
        时间复杂度：O(n)
        空间复杂度：O(n)
        技巧：压栈的时候先右孩子，再左孩子，从而左孩子先出栈。
        """
        self._preOrderNR(self._root)      # 调用self._preOrderNE函数

    def levelOrder(self):
        """
        层序遍历（广度优先遍历）
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        self._levelOrder(self._root)      # 调用self._levelOrder函数

    def minimum(self):
        """
        Description: 返回当前二叉搜索树的最小值
        时间复杂度：O(n)
        """
        if self.getSize() == 0:      # 空树直接报错
            raise Exception('Empty binary search tree!')
        return self._minmum(self._root).elem    # 调用self._minimum函数，它传入当前的根节点

    def maximum(self):
        """
        Description: 返回当前二叉搜索树的最大值
        时间复杂度：O(logn)
        """
        if self.getSize() == 0:     # 空树直接报错
            raise Exception('Empty binary search tree!')
        return self._maximum(self._root).elem           # 调用self._maxmum函数，它传入当前的根节点

    def removeMin(self):
        """
        Description: 删除当前二叉搜索树的最小值的节点
        时间复杂度：O(logn)
        Returns: 被删除节点所携带的元素的值
        """
        ret = self.minimum()    # 找到当前二叉搜索树的最小值
        self._root = self._removeMin(self._root)        # 调用self._removeMin函数，该函数返回删除节点后的二叉搜索树的根节点
        return ret  # 返回最小值

    def removeMax(self):
        """
       Description: 删除当前二叉搜索树的最大值的节点
       时间复杂度：O(logn)
       Returns: 被删除节点所携带的元素的值
       """
        ret = self.maximum()        # 找到当前二叉搜索树的最大值
        self._root = self._removeMax(self._root)        # 调用self._removeMax函数，该函数返回删除节点后的二叉搜索树的根节点
        return ret      # 返回最大值


    def remove(self,elem):
        """
        Description: 删除二叉搜索树中值为elem的节点，注意我们的二叉搜索树中的元素的值是不重复的，所以删除就是真正的删除，无残余
                     这个算法是二叉搜索树中最难的一个算法
                     note: 因为删除的是指定的值，用户已经直到该值了，所以就不需要返回这个值了。
                     时间复杂度：O(logn)
        """
        self._root=self._remove(self._root, elem)        # 调用self._remove函数，该函数返回删除节点后二叉搜索树的根节点

    def floor (self,elem):
        """
       Description: 找到elem在树中的floor值，关于floor与ceil的定义请自行百度。
       elem的floor值肯定是携带elem元素节点的左子树的最大值！想一想二分搜索树的性质！
       其实就是elem的前驱嘛
       时间复杂度：O(logn)
       Return:
       二分搜索树中elem元素的floor值
       """
        node = self._floor(self._root, elem)        # 调用self._floor函数
        if node is not None:                # 如果确实存在该元素的floor，就返回这个值
            return node.elem
        else:                       # 如果不存在该元素的floor，比如node是叶子节点，根本没有孩子，就返回None就好了
            return None

    def ceil(self,elem):
        """
       Description: 找到elem在树中的ceil值，关于floor与ceil的定义请自行百度。
       elem的ceil值肯定是携带elem元素节点的右子树的最小值！想一想二分搜索树的性质！
       其实就是elem的后继嘛
       相应的操作和floor类似，所以注释就少一些咯
       时间复杂度：O(logn)
       Return:
       二分搜索树中elem元素的ceil值
       """
        node = self._ceil(self._root,elem)       # 调用self._ceil函数
        if node is not None:
            return node.elem
        else:
            return None








        # private
    def _add(self, node, elem):
        """
        向以Node为根的二分搜索树插入元素elem，递归算法，这个根可以是任意节点哦，因为二分搜索树的每一个节点都是一个新的二分搜索树的根节点
        :param Node: 根节点
        :param elem: 带插入元素
        :return:     插入新节点后二分搜索树的根
        """
        if node is None:  # 递归到底的情况，此时已经到了None的位置。注意Node也算一棵二分搜索树
            self._size += 1  # 维护self._size
            return Node(elem)  # 新建一个携带elem的节点Node，并将它返回

        if elem < node.elem:  # 待添加元素小于当前节点的elem值
            node.left = self._add(node.left, elem)  # 继续递归向node的左子树添加elem，设想此时node.left已经为空，根据上面的语句，
            # 将返回一个新节点，而此时这个节点与二叉搜索树没有任何联系，所以要用node.left接住这个新节点，从而让新节点挂接到二叉搜索树上
        elif node.elem < elem:  # 当前节点的elem值小于待添加元素，原理同上
            node.right = self._add(node.right, elem)
        # 注意我们实现的是一个不带重复元素的二分搜索树，所以要用elif，而不是else，相当于对于插入了一个重复元素，我们什么也不做
        return node  # 最后要把node返回，还是这个根，满足定义。

    def _contains(self, node, elem):
        """
        在以node为根的二叉搜索树中查询是否包含元素elem
        :param node:    根节点
        :param elem:    带查找元素
        :return:        bool值，存在为True
        """
        if node is None:  # 递归到底的情况，已经到None了，还没有找到，返回False
            return False

        if node.elem < elem:  # 节点元素小于带查找元素，就向右子树的根节点递归查找
            return self._contains(node.right, elem)
        elif elem < node.elem:  # 带查找元素小于节点元素，就向左子树的根节点递归查找
            return self._contains(node.left, elem)
        else:  # 最后一种情况就是相等了，此时返回True
            return True

    def _preOrder(self, node):
        """
        对以node为根的节点的二叉搜索树的前序遍历
        :param node: 当前根节点
        """
        if node is None:  # 同样的，先写好递归到底的情况
            return
        print(node.elem, end=' ')  # 在这里我只是对当前节点进行了打印操作，并没有什么别的操作
        self._preOrder(node.left)  # 前序遍历以node.left为根节点的二叉搜索树
        self._preOrder(node.right)  # 最后才是右子树

    def _inOrder(self, node):
        """
        对以node为根节点的二叉搜索树的中序遍历
        :param node: 当前根节点
        """
        if node is None:  # 递归到底的情况
            return
        self._inOrder(node.left)  # 先左子树
        print(node.elem, end=' ')  # 再当前节点的操作，这里只是打印
        self._inOrder(node.right)  # 最后右子树

    def _postOrder(self, node):
        """
        对以node为根节点的二叉搜索树的后序遍历
        :param node: 当前根节点
        """
        if node is None:  # 递归到底的情况
            return
        self._postOrder(node.left)  # 先左子树
        self._postOrder(node.right)  # 再右子树
        print(node.elem, end=' ')  # 最后进行当前节点的操作

    def _preOrderNR(self, node):
        """
        对以node为根节点的二叉搜索树的非递归的前序遍历
        :param node: 当前根节点
        """
        stack = ArrayStack()  # 初始化一个我们以前实现的栈
        if node:
            stack.push(node)  # 如果根节点不为空，就首先入栈
        else:
            return
        while not stack.isEmpty():  # 栈始终不为空
            ret = stack.pop()  # 出栈并拿到栈顶的节点
            print(ret.elem, end=' ')  # 打印（我这里就只选择打印操作了，当然可以对这个节点执行任何你想要的操作）
            if ret.right:  # 出栈后，看一下ret的左右孩子，先入右孩子
                stack.push(ret.right)
            if ret.left:  # 再入栈左孩子，想想为什么是先右后左
                stack.push(ret.left)

    def _levelOrder(self, node):
        """
        Description: 对以node为根节点的二叉搜索树的广度优先遍历
        Params:
        - node: 当前根节点
        """
        if node is None:  # node本身就是None
            return
        queue = LoopQueue()  # 建立一个我们以前实现的循环队列，作为辅助数据结构
        queue.enqueue(node)  # 当前根节点入队
        while not queue.isEmpty():  # 如果队列不为空
            tmp_node = queue.dequeue()  # 取出队首的元素
            print(tmp_node.elem, end=' ')  # 这里仅仅是打印，无其他操作
            if tmp_node.left:  # 如果左孩子不是None
                queue.enqueue(tmp_node.left)  # 将它的左孩子入队，注意是先左孩子后右孩子哦，想象为什么是这样
            if tmp_node.right:  # 如果右孩子不是None
                queue.enqueue(tmp_node.right)  # 右孩子入队

    def _minmum(self,node):
        """
        Description: 返回以node为根的二叉搜索树携带最小值的节点
        """

        if node.left is None:       # 递归到底的情况，二叉搜索树的最小值就从当前节点一直向左孩子查找就好了
            return node
        return self._minmum(node.left)      # 否则向该节点的左子树继续查找

    def _maximum(self, node):
        """
        Description: 返回以node为根的二叉搜索树携带最大值的节点
        """
        if node.right is None:      # 递归到底的情况，二叉搜索树的最大值就从当前节点一直向右孩子查找就好了
            return node
        return self._maximum(node.right)    # 否则向该节点的右子树继续查找

    def _removeMin(self,node):
        """
       Descriptoon: 删除以node为根节点的二叉搜索树携带最小值的节点
       Returns: 删除后的二叉搜索树的根节点，与添加操作有异曲同工之处
       """
        if node.left is None:           # 递归到底的情况
            right_node = node.right      # 记录当前节点的右节点，即使是None也没关系
            node.right = None           # 将当前节点的右节点置为None，便于垃圾回收
            self._size -=1               # 维护self._size
            return right_node           # 返回当前节点的右子树的根，因为删除最小节点有两种情况，一种是node是叶子节点，直接用None来代替就好了。另外一种就是node还有右子树
                                         # 此时需要用node的右节点来代替当前的节点
        node.left = self._removeMin(node.left)      # 没到底就继续向左子树前进，注意要用node.left接住被删除节点的右节点，从而与整棵树产生连接。
        return node             # 将节点返回，从而在递归算法完成后的回归过程中逐层返回直到最后到根节点

    def _removeMax(self, node):
        """
       Description: 删除以node为根节点的二叉搜索树携带最大值的节点
       Returns: 删除后的二叉搜索树的根节点，与添加操作有异曲同工之处
       """

        if node.right is None:           # 与self.removeMin原理差不多，不再赘述
            left_node = node.left
            node.left = None
            self._size -=1
            return left_node

        node.right = self._removeMax(node.right)
        return node

    def _remove(self,node, elem):
        """
        Description: 删除以node为根节点的二叉搜索树中携带值为elem的节点
        Returns: 删除节点后的二叉搜索树的根节点
        """
        if node is None:        # 没找到携带elem的节点
            return None

        if elem < node.elem:        # 要寻找的元素小于当前节点的elem值
            node.left = self._remove(node.left, elem)       # 向node的左子树继续寻找，注意要用node.left接住返回值，从而让代替被删除节点的节点与搜索树产生连接
            return node             # 返回node，从而在递归完事后的回归过程中最终返回到搜索树的根节点
        elif node.elem < elem: #同理
            node.right = self._remove(node.right,elem)
            return node

        else:       # 此时 elem == node.elem
            if node.left is None:       # node左子树为空的情况，单独处理，与前面的删除最大/最小节点的方法一致，不再赘述
                ret = node.right
                node.right = None
                self._size -= 1
                return ret
            elif node.right is None:        # node右子树为空的情况
                ret = node.left
                node.left = None
                self._size -=1
                return ret
            else:   # 此时node左右子树均不为空，此时是该算法重头戏
                # 既然node的左右子树均不为空，那么删除node后究竟要用谁来接替这个删除后的空位呢，答案是node的前驱或者后继节点！前驱节点就是node左子树携带最大值的节点
                # 这个节点满足：它的elem一定小于node右子树全部元素的elem，但是还大于左子树全部元素的elem（除了他自己--），同理后继是node右子树的最小值，代替
                # node后也满足二叉搜索树的要求，本文通过node的后继来实现，小伙伴们可以用前驱来实现，也非常简单。
                successor=self._minmum(node.right)      # 通过self._minimum方法找到node的后继节点，并记为seccessor
                successor.right = self._removeMin(node.right)        # 通过self._removeMin方法将node的右子树的最小节点删除，注意返回的删除节点的新的右子树的根节点，所以
                # 此时直接将返回值作为successor的右节点就可以了
                self._size +=1      # 但是我们的目的是让后继来取代被删除的位置的节点，并不是要删除它，而self._removeMin方法中已经对self._size进行了维护，所以在这里我们要加回来
                successor.left = node.left           # successor的左孩子就是node的左孩子就好了，代替嘛，画个图看看就懂啦
                node.left =node.right = None        # 可以把node扔了，他已经没用了，让node从树中脱离
                self._size -=1                      # 把二叉搜索树上的节点都扔了，肯定要维护一下self._size
                return successor                    # 返回取代node后的后继节点

    def _floor(self, node, elem):
        """
        Description: 获取以node为根的二分搜索树携带elem节点的floor值的节点
        Params:
        - elem: 带查找元素
        Returns:
        携带elem的floor值的节点
        """
        if node is None:    # 到头了还没找到elem，报错就完事了
            raise Exception('Error, the %s is not in BST!, please check again.' % elem)

        if elem < node.elem:                # 先要找到携带elem元素的节点，所以此时往左子树深入
            return self._floor(node.left, elem)
        elif node.elem < elem:      # 此时往右子树深入
            return self._floor(node.right, elem)
        else:                       # 此时node.elem == elem了，有两种情况呢
            if node.left is None:        # 第一种这个node并没有左子树，没有左孩子，所以返回None就好了
                return None             # 此时node还有左子树，那就找到node左子树携带最大值的节点
            return self._maximum(node.left)          # 调用self._maximum函数找到node左子树中携带最大值的节点


    def _ceil(self, node, elem):
        """
        Description: 获取以node为根的二分搜索树携带elem节点的ceil值的节点
        Params:
        - elem: 带查找元素
        Returns:
        携带elem的ceil值的节点
        """
        if node is None:
            raise Exception('Error, the %s is not in BST!, please check again.' % elem)

        if elem < node.elem:
            return self._ceil(node.left,elem)
        elif node.elem < elem:
            return self._ceil(node.right,elem)
        else:    # node.elem == elem
            if node.right is None:           # 此时node没有右子树，也就没有什么所谓的ceil
                return None    #返回None
            else:       #此时是有右子树的
                return self._minmum(node.right)         # 调用self._minimum函数找到node右子树中携带最小值的节点



if __name__ == '__main__':
    test_bst = BST()
    print('初始大小：', test_bst.getSize())
    print('是否为空：', test_bst.isEmpty())

    add_list = [15, 4, 25, 22, 3, 19, 23, 7, 28, 24]
    print('待添加元素：', add_list)
    for add_elem in add_list:
        test_bst.add(add_elem)

    print('添加元素后，树的大小：', test_bst.getSize())
    print('是否包含28？', test_bst.contains(28))
    print('前序遍历：（递归版本）')
    test_bst.preOrfer()
    print()  # 为了美观，起换行作用
    print('前序遍历：（非递归版本)')
    test_bst.preOrderNR()
    print()
    print('中序遍历：')
    test_bst.inOrder()
    print()
    print('后序遍历：')
    test_bst.postOrder()
    print()
    print('广度优先遍历（层序遍历）：')
    test_bst.levelOrder()
    print()
    print('树中最小值：', test_bst.minimum())
    print('树中最大值：', test_bst.maximum())
    print('25的floor值：', test_bst.floor(25))
    print('15的ceil值：', test_bst.ceil(15))
    print('-------------------------------------------')
    print('删除最小值后的层序遍历以及树的大小')
    print('删除的最小值为：', test_bst.removeMin())
    print('层序遍历：', end=' ')
    test_bst.levelOrder()
    print()
    print('最小值删除后的size：', test_bst.getSize())
    print('-------------------------------------------')
    print('删除最大值后的层序遍历以及树的大小')
    print('删除的最大值为：', test_bst.removeMax())
    print('层序遍历：', end=' ')
    test_bst.levelOrder()
    print()
    print('最大值删除后的size：', test_bst.getSize())
    print('-------------------------------------------')
    print('删除特定元素22，以及删除后树的大小')
    test_bst.remove(22)
    print('层序遍历：', end=' ')
    test_bst.levelOrder()
    print()
    print('删除22后的size:', test_bst.getSize())
    print('-------------------------------------------')


