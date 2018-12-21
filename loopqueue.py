class LoopQueue:
    def __init__(self, capacity=10):
        """
        构造函数
        :param capacity: 循环队列的初始容量，默认为10。
        """
        self._capacity = capacity + 1   # 对于用户来说，其容量为capacity。而对于内部实现来说，需要满足判空与判满的奇异性，
        # 当self._tail + 1 = self._front是，此时判定为满，此时还剩余一个空间，所以真实容量是用户指定容量加一！
        self._front = 0     # 队首的索引（闭区间）
        self._tail = 0      # 队尾的索引（开区间，就像C++的.end()迭代器那样）self._front=self._tail=0，即初始化为空
        self._data = [float('nan')] * self._capacity  # 初始化为nan * self._capacity这么多容量
        # tip:其实完全可以加入self._size来更好的阐述循环队列，有了这个成员变量循环队列的操作也变得简单了许多，而且定义
        # 也更加清晰，但是为了阐述循环队列底层的工作原理，应用self._front和self._tail完全可以表述self._size。这样
        # 我认为会对循环队列有着更深的认识。如果没有self._size这一成员变量，主要有两个坑：
        # 1. self._size的求法。
        # 2. self._resize的时候有大坑！！！真的对程序debug的能力有了提升--

    def isEmpty(self):
        """
        判断循环队列是否为空
        :return: bool值，空为True
        """
        return self._front == self._tail    # self._tail和self._tail相等时表示空。

    def getCapacity(self):
        """
        获取循环队列当前的容量
        :return: 循环队列的容量
        """
        return self._capacity - 1   # 对于用户来说得到的容量需要减一哦

    def getSize(self):
        """
        获得循环队列内有效元素的个数
        :return: 有效元素的个数
        """
        retSize = None      # 要返回的size
        if self._tail >= self._front:            # self._tail在self._front后面（包括等于），就和普通队列一样
            retSize = self._tail - self._front
        else:           # 此时self._front > self._tail
            retSize = self._capacity - (self._front - self._tail)  # 讲过啦，很简单
        return retSize

    def enqueue(self, elem):
        """
        将元素elem入队
        时间复杂度：O(1)
        :param elem: 要入队的元素
        """
        if (self._tail + 1) % self._capacity == self._front:    # 满了
            self._resize(self.getCapacity() * 2)        # 扩大为getCapacity()的两倍
            # 解释一下这里为什么不是self._capacity * 2。首先self._capacity和self.getCapacity()之间差一个1，
            # 其次此时真实可容纳元素的空间是self.getCapacity()，扩大为它的二倍，也就是此时真实可容纳元素的空间
            # 变为原先的两倍，self._capacity也容易维护，只需加一即可。
        self._data[self._tail] = elem   # 将self._tail的位置的元素置为elem
        self._tail = (self._tail + 1) % self._capacity # 维护self._tail，注意是循环队列哦，要对全体空间取余的！

    def dequeue(self):
        """
        循环队列的出队操作
        时间复杂度：O(1)
        :return: 出队元素的值
        """
        if self.isEmpty():      # 队列此时没有元素
            raise Exception('Error.The loop queue is empty, can not make dequeue operation.')   # 抛出异常
        ret_val = self._data[self._front]   # 记录一下队首的元素，方便返回
        self._data[self._front] = None  # 手动回收self._front处的元素
        self._front = (self._front + 1) % self._capacity    # 维护self._front，直接加一就好，注意循环队列的性质，要对
        # 全体空间取余

        if self.getSize() and self.getCapacity() // self.getSize() == 4:    # 队列不为空且有效元素个数为可容纳元素的四分之一时，缩容
            self._resize(self.getCapacity() // 2)   # 缩容为原先的二分之一
        return ret_val  # 返回队首元素

    def getFront(self):
        """
        获取队首的元素的值（队列一般只关心队首）
        :return: 队首元素的值
        """
        if self.isEmpty():      # 空队列抛异常就完事了
            raise Exception('Error. The loop queue is empty, can not get any mumber.')
        return self._data[self._front]  # 获得self._front索引处的元素

    def printLoopQueue(self):
        """对循环队列内的有效元素进行打印操作"""
        print('LoopQueue: Front--- ', end='')       # 队首
        index = self._front     # 从队首开始
        while index != self._tail:  # 没到达队尾就一直打印
            if index + 1 != self._tail:     # 没到最后一次的打印。为了对称，强迫症。。
                print(self._data[index], end='  ')      # 打印当前元素
                index = (index + 1) % self._capacity    # index向后推进，注意是循环队列，到self._data的尾部就要返回到0索引处哦，
                # 所以要对真实的存储空间取余，而不是对self.getCapacity()取余！这么做就错了！
            else:
                print(self._data[index], end=' ')
                break       # 最后一次打印操作，完事直接退出循环就好
        print('---Tail')    # 队尾
        print('Size: %d， Capacity: %d' % (self.getSize(), self.getCapacity()))  # 有效元素个数以及当前容量的打印


    # private
    def _resize(self, capacity):
        """
        扩/缩容操作，将容量扩/缩至capacity（这里的capacity是面向用户，所以真正的self._capaciry应该是capacity+1，才能容纳capacity这么多元素呀）
        :param capacity: 新的容量（基于用户的角度）
        """
        # 此时千万不能先做self._capacity = capacity + 1 。因为一会儿要将当前队列中的元素全部取出来，一旦
        # self._tail在self._front的前面，而self._capacity已经改变，就不能全部取出来了！好好想一下～以前就进过坑
        tmp_list = [float('nan')] * (capacity + 1)  # 建立一个新的list，真实容量为capacity+1，原因你懂得
        index = self._front     # 准备开始遍历原先的self._data，转移元素！从self._front开始
        while index != self._tail:  # 若index一直没到self._tail，就继续往后撸
            tmp_list[index - self._front] = self._data[index]  # 注意在这里我把原先的元素都放到新list的以索引零开始的地方顺序的放置元素
            index = (index + 1) % self._capacity    # index往后撸，注意循环队列的性质。
        self._data = tmp_list           # 更新self._dat为新的那个数据，self._data会被自动垃圾回收的，不用担心它。


        self._tail = self.getSize()     # 维护self._tail。就是 0 + self.getSize()。因为转移元素并不改变size呀。
        self._front = 0                 # 维护self._front，因为我是从零开始放的，所以置零。
        # 我把上面这两句单拿出来说明，原因很简单……有大坑！！尼玛找bug找了半个小时--。。
        # 这两句话的顺序一定不能变！变了对扩容没有影响，但是缩容就会出错！虽然我们心里知道是从零开始放的，但是应该先安排self._tail。因为
        # 一旦先把self._front置零，geiSize()方法瞬间出错！随后调用self.getSize()就出现问题了！导致self._tail出现在缩容后数组
        # 索引的overflow位置，打印的话就会无线循环打印！因为self._front始终不能等于self._tail呀！所以一定要先安排self._tail！

        self._capacity = capacity + 1   # 最后再维护self._capacity！讲过了，前面的很多操作依赖于原先的最大容量，等他们都完事了，最后维护这个


if __name__ == '__main__':
    testLoopQueue = LoopQueue()
    print('入队15次：')
    for i in range(15):
        testLoopQueue.enqueue(i)
    print('front:', testLoopQueue._front)
    print('tail:', testLoopQueue._tail)
    print('队列元素打印：', end=' ')
    testLoopQueue.printLoopQueue()

    print('出队12次：')
    docker = []
    for i in range(12):
        docker.append(testLoopQueue.dequeue())
        print('steps: %d, front: %d, tail: %d, Size: %d, Capacity: %d' % (i + 1, testLoopQueue._front, testLoopQueue._tail, testLoopQueue.getSize(), testLoopQueue.getCapacity()))
    print('出队docker:', docker)
    print('队列元素打印：', end=' ')
    testLoopQueue.printLoopQueue()
    print('队首元素：', testLoopQueue.getFront())




