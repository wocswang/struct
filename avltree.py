"""实现一个自平衡的AVLtree"""
from collections import deque, Iterable
import pygraphviz as pgv
import random


class Node(object):
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key          # 存储的数据
        self.parent = parent    # 父节点
        self.left = left        # 左孩子节点
        self.right = right      # 右孩子节点
        self.bf = 0             # 平衡因子 等于左子树高度减去右子树高度


class AVLTree(object):
    def __init__(self, key=None):
        if key:
            self.root = Node(key)
        else:
            self.root = None

    def insert(self, *keys):
        """插入键值，键可以是个可迭代对象，或是多个独立的键"""
        if isinstance(keys[0], Iterable):
            if len(keys) > 1:
                print("插入失败...第一个参数可迭代对象时参数只能有一个")
                return
            keys = keys[0]
        else:
            keys = keys
        for key in keys:
            if not self.root:
                self.root = Node(key)
            else:
                p = self.root
                while 1:
                    if key == p.key:
                        print("%d键已存在, 跳过该键" % key)
                        break
                    elif key < p.key:
                        if not p.left:                  # 当前左节点可以添加
                            cur_node = Node(key, p)
                            p.left = cur_node
                            self.balance_by_insert(cur_node)
                            break
                        else:
                            p = p.left
                    else:
                        if not p.right:
                            cur_node = Node(key, p)
                            p.right = cur_node
                            self.balance_by_insert(cur_node)
                            break
                        else:
                            p = p.right

    def balance_by_insert(self, cur):
        """
        更新插入后的平衡因子, 平衡二叉树
        :param cur: 当前插入节点cur
        :return: None
        """
        par = cur.parent                        # 插入节点的父节点
        while par:
            if cur == par.left:                 # 如果当前节点是父节点的左节点
                par.bf -= 1
            else:
                par.bf += 1
            if par.bf == 0:                     # 为0说明没有增加树的高度, 返回
                return
            if par.bf == -2:
                if cur.bf == 1:                 # 左右双向旋转
                    self.lr_rotate(par, cur)
                    break
                else:
                    self.r_rotate(par, cur)
                    break
            elif par.bf == 2:
                if cur.bf == -1:                # 左右双向旋转
                    self.rl_rotate(par, cur)
                    break
                else:
                    self.l_rotate(par, cur)
                    break
            cur = par                           # 从添加的节点开始往上更新直到根节点
            par = par.parent

    def balance_by_delete(self, cur):
        """根据删除节点位置向上更新平衡因子"""
        par = cur.parent
        while par:
            if cur == par.left:                 # 如果当前节点是父节点的左节点
                par.bf += 1
            else:
                par.bf -= 1
            if par.bf == 1 or par.bf == -1:     # 为0说明没有增加树的高度, 返回
                return
            if par.bf == -2:
                cur = cur.parent.left           # 旋转是旋转与插入方向相反的两个节点
                if cur.bf == 1:                 # 左右双向旋转
                    self.lr_rotate(par, cur)
                    par = cur.parent            # 更新一下par的指向
                elif cur.bf == 0:
                    self.r_rotate(par, cur)     # 特殊情况树的高度并没有增加需要退出往上更新
                    cur.bf = 1
                    par.bf = -1
                    break
                else:
                    self.r_rotate(par, cur)
                    par = cur
            elif par.bf == 2:
                cur = cur.parent.right
                if cur.bf == -1:                # 左右双向旋转
                    self.rl_rotate(par, cur)
                    par = cur.parent            # 更新一下par的指向
                elif cur.bf == 0:
                    self.l_rotate(par, cur)
                    cur.bf = -1
                    par.bf = 1
                    break
                else:
                    self.l_rotate(par, cur)
                    par = cur
            cur = par                           # 从添加的节点开始往上更新直到根节点
            par = par.parent

    def delete_key(self, key):
        """删除键值, 通过三个子函数实现功能处理三种情况"""

        def first(node):
            """第一种情况, 找到的键本身是叶节点, 直接删除"""
            self.balance_by_delete(node)
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
            del node

        def second(node):
            """第二种, 找到的键本身带有左子节点或右子节点"""
            par = node.parent                    # 获得该键的父节点引用
            if node.left:                        # 该节点只有左节点
                if par is None:                  # 说明该节点是root
                    self.root = node.left
                    node.left.parent = None
                elif node == par.left:           # 该节点是父节点的左节点
                    par.left = node.left
                    node.left.parent = par
                else:
                    par.right = node.left
                    node.left.parent = par
                self.balance_by_delete(node.left)
            else:
                if par is None:
                    self.root = node.right
                    node.left.parent = None
                elif node == par.left:
                    par.left = node.right
                    node.right.parent = par
                else:
                    par.right = node.right
                    node.right.parent = par
                self.balance_by_delete(node.right)
            del node

        def third(node):
            p = node.left                         # 寻找左边最大的子节点代替
            while p.right:
                p = p.right                       # 寻找最大子节点

            node.key, p.key = p.key, node.key     # 交换两个节点，这里的交换取了个巧，只交换值就不用处理节点之间的复杂关系了
            if p.left or p.right:                 # 转换为第二种或第一种情况
                second(p)
            else:
                first(p)

        cur = self.find(key)                      # 寻找要删除的值
        if cur:
            if cur.left and cur.right:
                third(cur)
            elif not cur.left and not cur.right:  # 直接是叶节点, 第一种情况
                first(cur)
            else:                                 # 第二种情况, 只有左节点或右节点
                second(cur)
        else:
            print("键值不存在, 删除失败")

    def find(self, key):
        """寻找键值"""
        p = self.root
        while p:
            if p.key == key:
                return p
            if key < p.key:
                p = p.left
            else:
                p = p.right
        return None

    def r_rotate(self, par, cur):
        """右单旋转"""
        p = cur.right
        cur.right = par
        par.left = p
        if p:
            p.parent = par
        if par == self.root:
            self.root = cur
        else:
            if par == par.parent.left:
                par.parent.left = cur
            else:
                par.parent.right = cur

        cur.parent = par.parent         # 更新父节点信息
        par.parent = cur
        cur.bf = par.bf = 0         # 更新平衡因子

    def l_rotate(self, par, cur):
        """
        左单旋转
        :param par:  平衡因子为2|-2的节点
        :param cur:  作为轴心旋转的节点(平衡因子不为2)
        :return: None
        """
        p = cur.left                    # 辅助引用p指向cur的左节点
        cur.left = par                  # cur的左节点指向par
        par.right = p                   # par的右节点指向cur的左节点
        if p:
            p.parent = par              # cur的左节点不为空时更新该节点的父节点
        if par == self.root:
            self.root = cur             # 判断平衡因子为2的par是否为根
        else:
            if par == par.parent.left:  # 更新par父节点的子节点信息
                par.parent.left = cur
            else:
                par.parent.right = cur
        cur.parent = par.parent         # 当前cur的父节点指向原来par的父节点
        par.parent = cur                # par变为cur的左子节点

        cur.bf = par.bf = 0         # 插入操作中, 操作的两个节点旋转后平衡因子恢复为0

    def lr_rotate(self, par, cur):
        """左右双旋转"""
        # 先左旋转 cur 和 cur的右子节点
        cur_right = cur.right           # 获得cur的右子节点的引用
        bf = cur_right.bf
        self.l_rotate(cur, cur_right)
        # 继续右旋转
        self.r_rotate(par, cur_right)
        if bf == 0:                     # 根据cur_right的平衡因子更新操作的3个节点
            cur.bf = cur_right.bf = par.bf = 0
        elif bf == -1:
            par.bf = 1
            cur.bf = cur_right.bf = 0
        else:
            cur.bf = -1
            cur_right.bf = par.bf = 0

    def rl_rotate(self, par, cur):
        """右左双旋转"""
        # 先右旋转 cur 和 cur的左子节点
        cur_left = cur.left                         # 获得cur的右子节点的引用
        bf = cur_left.bf
        self.r_rotate(cur, cur_left)
        self.l_rotate(par, cur_left)                # 继续右旋转
        if bf == 0:                                 # 根据cur_left的平衡因子更新操作的3个节点
            cur.bf = cur_left.bf = par.bf = 0
        elif bf == -1:
            cur.bf = 1
            par.bf = cur_left.bf = 0
        else:
            par.bf = -1
            cur_left.bf = cur.bf = 0

    def get_tree_state(self, _tree=None):
        """返回树的高度和元素数量和树是否平衡组成的一个元组"""
        if not _tree:
            _tree = self.root
        count = 0
        is_balanced = True

        def get_state(_tree):
            nonlocal count, is_balanced
            if not _tree:
                return 0
            count += 1
            h1 = get_state(_tree.left) + 1
            h2 = get_state(_tree.right) + 1
            if abs(h1 - h2) >= 2:
                is_balanced = False
            return max((h1, h2))
        return get_state(_tree), count, is_balanced

    def pre_traversal(self):
        """先序遍历"""
        def traver(node):
            if node:
                print(node.key, end=' ')
                traver(node.left)
                traver(node.right)

        traver(self.root)
        print()

    def in_order_traversal(self):
        """中序遍历"""
        _node = self.root

        def traver(node):
            if node:
                traver(node.left)
                print(node.key, end=' ')
                traver(node.right)

        traver(_node)
        print()

    def level_traversal(self):
        """层次遍历, 自己简单把树分层打印出来"""
        d = deque()
        d.append((1, 1, self.root))                 # 元组表示第1层第1个数
        level = 2
        level_count = 0                             # 每层的数量
        last_l = 1
        while d:
            # p = d.popleft()
            ll, c, p = d.popleft()
            if ll != last_l:
                last_l = ll
                print("")
            # print(p.key, 'bf: %s' % p.bf, end=' ')
            print(p.key, end=' ')
            level_count += 1
            if p.left:
                d.append((level, level_count, p.left))

            level_count += 1
            if p.right:
                d.append((level, level_count, p.right))
            if level_count == pow(2, level-1):
                level_count = 0
                level += 1
        print()

    def draw(self, filename='./tree.png'):
        """生成二叉树的图片文件"""
        g = pgv.AGraph(strict=False, directed=True)
        g.node_attr['shape'] = 'circle'

        def traver(node):
            if node:
                if not node.parent:
                    g.add_node(node.key)
                else:
                    g.add_edge(node.parent.key, node.key)
                traver(node.left)
                traver(node.right)

        traver(self.root)
        g.layout('dot')
        g.draw(filename)


if __name__ =='__main__':
    import random
    import os

    path = './tree_pic'
    if not os.path.exists(path):
        os.mkdir(path)

    g = (path + '/tree' + str(i) + '.png' for i in range(1, 30))

    t = AVLTree()

    lst = random.sample(range(30, 300), 20)
    t.insert(lst)
    print(lst)
    t.draw(next(g))
    print(t.get_tree_state())
    for i in range(8):
        k = random.choice(lst)
        print("删除键%d" % k)
        t.delete_key(k)
        print(t.get_tree_state())           # 打印树的高度, 元素个数，树是否平衡
        t.draw(next(g))


    t.insert(-5,200,300)
    t.insert(10,0,410,15,500)
    t.draw(next(g))
    print(t.get_tree_state())