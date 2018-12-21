# -*- coding: utf-8 -*-
import pygraphviz as pgv
import itertools
class RBTree(object):
    def __init__(self):
        self.nil = RBTreeNode(0)
        self.root = self.nil

class RBTreeNode(object):
    def __init__(self,x):
        self.key = x
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'black'
        self.size = None

#左旋转
def LeftRotate(T, x):
    y = x.right
    x.right = y.left
    if y.left != T.nil:
        y.left.parent = x
    y.parent = x.parent
    if x.parent == T.nil:
        T.root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent =y

#右旋转
def RightRotate(T, x):
    y = x.left
    x.left = y.right
    if y.right !=T.nil:
        y.right.parent = x
    y.parent = x.parent
    if x.parent == T.nil:
        T.root = y
    elif x == x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y

    y.right = x
    x.parent = y

#红黑树的插入
def RBInsert(T, z):
    y = T.nil
    x = T.root
    while x != T.nil:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y == T.nil:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    z.left = T.nil
    z.right = T.nil
    z.color = 'red'
    RBInsertFixup(T, z)
    return z.key, '颜色为', z.color


def RBInsertFixup(T, z):
    while z.parent.color == 'red':
        if z.parent == z.parent.parent.left:
            y = z.parent.parent.right
            if y.color == 'red':
                z.parent.color = 'black'
                y.color = 'black'
                z.parent.parent.color = 'red'
                z= z.parent.parent
            else:
                if z == z.parent.right:
                    z = z.parent
                    LeftRotate(T, z)
                z.parent.color = 'black'
                z.parent.parent.color = 'red'
                RightRotate(T, z.parent.parent)

        else:
            y = z.parent.parent.left
            if y.color == 'red':
                z.parent.color = 'black'
                y.color = 'black'
                z.parent.parent.color = 'red'
                z = z.parent.parent

            else:
                if z == z.parent.left:
                    z = z.parent
                    RightRotate(T, z)
                z.parent.color = 'black'
                z.parent.parent.color = 'red'
                LeftRotate(T, z.parent.parent)
    T.root.color = 'black'

def RBTransplant(T, u, v):
    if u.parent == T.nil:
        T.root = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v

    v.parent = u.parent


def RBDelete(T, z):
    y=z
    y_original_color = y.color
    if z.left == T.nil:
        x = z.right
        RBTransplant(T, z, z.right)
    elif z.right == T.nil:
        x = z.left
        RBTransplant(T, z, z.left)

    else:
        y = TreeMinimum(z.right)
        y_original_color = y.color
        x = y.right
        if y.parent == z:
            x.parent = y
        else:
            RBTransplant(T, y, y.right)
            y.right = z.right
            y.right.parent = y
        RBTransplant(T, z, y)
        y.left = z.left
        y.left.parent = y
        y.color = z.color

    if y_original_color == 'black':
        RBDeleteFixup(T, x)

#红黑树的删除
def RBDeleteFixup(T, x):
    while x != T.root and x.color == 'black':
        if x == x.parent.left:
            w = x.parent.right
            if w.color == 'red':
                w.color = 'black'
                x.parent.color = 'red'
                LeftRotate(T, x.parent)
                w = x.parent.right

            if w.left.color == 'black' and w.right.color =='black':
                w.color = 'red'
                x = x.parent
            else:
                if w.right.color == 'black':
                    w.left.color = 'black'
                    w.color = 'red'
                    RightRotate(T, w)
                    w = x.parent.right
                w.color = x.parent.color
                x.parent.color = 'black'
                w.right.color = 'black'
                LeftRotate(T, x.parent)
                x = T.root

        else:
            w = x.parent.left
            if w.color == 'red':
                w.color = 'black'
                x.parent.color = 'red'
                RightRotate(T, x.parent)
                w = x.parent.left

            if w.right.color == 'black' and w.left.color =='black':
                w.color = 'red'
                x = x.parent

            else:
                if w.left.color == 'black':
                    w.right.color = 'black'
                    w.color = 'red'
                    LeftRotate(T, w)
                    w = x.parent.left

                w.color = x.parent.color
                x.parent.color = 'black'
                w.left.color = 'black'
                RightRotate(T, x.parent)
                x = T.root
    x.color = 'black'


def TreeMinimum(x):
    while x.left != T.nil:
        x = x.left
    return x



#中序遍历
def Midsort(x):
    if x!=None:
        Midsort(x.left)
        if x.key !=0:
            print('key:', x.key, 'x.parent',x.parent.key)
        Midsort(x.right)


def draw(filename='./tree.png',draw_nil=0):
    if T.root == T.nil:
        return
    graph = pgv.AGraph(strict=False, directed=True)
    graph.node_attr.update({
        'shape': 'circle',
        'style': 'filled',
        'fontcolor': 'white',
    })
    graph.add_node(T.root.key, color=T.root.color)
    if draw_nil == 0:
        draw_subtree(T.root, graph)
    elif draw_nil == 1:
        # use one nil node for leaves and parent of root
        graph.add_node('nil1', color='black', label='nil')
        graph.add_edge('nil1', T.root.key)
        draw_subtree(T.root, graph, draw_nil)
    else:
        # use different nil nodes for leaves and parent of root
        graph.add_node('nil1', color='black', label='nil')
        graph.add_edge('nil1', T.root.key)
        draw_subtree(T.root, graph, draw_nil, counter=itertools.count(2))
    # print(graph.string())
    graph.draw(filename, prog='dot')


def draw_subtree(node, graph, draw_nil=0, counter=None):
    if node == T.nil:
        return
    if node.left != T.nil:
        graph.add_node(node.left.key, color=node.left.color)
        graph.add_edge(node.key, node.left.key, tailport='sw')
        draw_subtree(node.left, graph, draw_nil, counter)
    elif draw_nil == 1:
        graph.add_edge(node.key, 'nil1', tailport='sw')
    elif draw_nil == 2 and counter is not None:
        nil_id = 'nil%d' % next(counter)
        graph.add_node(nil_id, color='black', label='nil')
        graph.add_edge(node.key, nil_id, tailport='sw')

    if node.right != T.nil:
        graph.add_node(node.right.key, color=node.right.color)
        graph.add_edge(node.key, node.right.key, tailport='se')
        draw_subtree(node.right, graph, draw_nil, counter)
    elif draw_nil == 1:
        graph.add_edge(node.key, 'nil1', tailport='se')
    elif draw_nil == 2 and counter is not None:
        nil_id = 'nil%d' % next(counter)
        graph.add_node(nil_id, color='black', label='nil')
        graph.add_edge(node.key, nil_id, tailport='se')

if __name__ =='__main__':
    import os

    path = './rbtree_pic'
    if not os.path.exists(path):
        os.mkdir(path)
    # g = (path + '/tree' + str(i) + '.png' for i in range(1, 30))
    g=(path+'/tree'+str(i)+'.png' for i in range(1,30))

    nodes = [11,2,14,1,7,15,5,8,4]
    T = RBTree()

    for node in nodes:
        print('插入数据', RBInsert(T, RBTreeNode(node)))

    print('中序遍历')
    Midsort(T.root)
    RBDelete(T,T.root)
    print('中序遍历')
    Midsort(T.root)
    RBDelete(T,T.root)
    print('中序遍历')
    Midsort(T.root)

    draw(filename=next(g), draw_nil=0)
    draw(filename=next(g), draw_nil=1)
    draw(filename=next(g), draw_nil=2)