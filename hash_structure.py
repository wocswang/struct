# -*- coding: utf-8 -*-
class LinearMap(object):
    def __init__(self):
        self.items = []

    # 往表中添加元素
    def add(self, k, v):
        self.items.append((k, v))

    # 线性方式查找元素
    def get(self, k):
        for key, value in self.items:
            if key == k:  # 键存在，返回值，否则抛出异常
                return value
        raise KeyError


class BetterMap(object):
    # 利用 LinearMap 对象作为子表，建立更快的查询表
    def __init__(self,n=100):
        self.maps = []          # 总表格
        for i in range(n):      # 根据n的大小建立n个空的子表
            self.maps.append(LinearMap())

    def find_map(self,k):            # 通过hash函数计算索引值
        index = hash(k) % len(self.maps)
        return self.maps[index]         #返回索引子表的引用

        # 寻找合适的子表（linearMap对象）,进行添加和查找
    def add(self,k,v):
        m = self.find_map(k)
        m.add(k,v)

    def get(self, k):
        m = self.find_map(k)
        return m.get(k)



class HashMap(object):
    #初始化总表为，容量为2的表格（含两个子表）
    def __init__(self):
        self.maps = BetterMap(2)
        self.num = 0

    def get(self,k):
        return self.maps.get(k)

    # 若当前元素数量达到临界值（子表总数）时，进行重排操作
    # 对总表进行扩张，增加子表的个数为当前元素个数的两倍！
    def add(self, k, v):
        if self.num == len(self.maps.maps):
            self.resize()

        self.maps.add(k,v)      # 往重排过后的 self.map 添加新的元素
        self.num +=1


    # 重排操作，添加新表, 注意重排需要线性的时间
    # 先建立一个新的表,子表数 = 2 * 元素个数
    def resize(self):
        new_maps = BetterMap(self.num *2)

        for m in self.maps.maps:        # 检索每个旧的子表
            for k,v in m.items:         # 将子表的元素复制到新子表
                new_maps.add(k,v)

        self.maps = new_maps


