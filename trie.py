# -*- coding: utf-8 -*-
class Trie:
    def __init__(self):
        """
        在这里初始化数据结构
        """
        self.root = {}
        self.word_end = -1
        self._size=0

    def getSize(self):
        """
        获取树中个数
        :return: num
        """
        return self._size

    def insert(self, word):
        """
        插入一个单词
        :param word: str
        :return: void
        """
        node = self.root
        for chars in word:
            child = node.get(chars)
            if not child:
                node[chars] = {}
            node= node[chars]
        node[self.word_end] = True
        self._size += 1


    def contains(self,word):
        """
        查询单词
        :param word: str
        :return: bool
        """
        node = self.root
        for chars in word:
            node = node.get(chars)
            if not node:
                 return False
        return True



    def startsWith(self, prefix):
        """
        查找前缀树的单词
        :param prefix: str
        :return: bool
        """
        node = self.root
        for chars in prefix:
            node = node.get(chars)
            if not node:
                return False

        return True



    def get_start(self, prefix):
        """
        返回前缀树的单词
        :param prefix:
        :return: words(list)
        """

        def get_key(pre, pre_node):
            word_list=[]
            if pre_node.is_word:
                word_list.append(pre)

            for x in pre_node.keys():
                word_list.extend(get_key(pre + str(x), pre_node.get(x)))
            return word_list

        words = []
        if not self.startsWith(prefix):
            return words
        if self.contains(prefix):
            words.append(prefix)
            return words

        node = self.root
        for chars in prefix:
            node = node.get(chars)

        return get_key(prefix, node)

if __name__=='__main__':
    test_trie = Trie()
    test_trie.insert('something')
    test_trie.insert('somebody')
    test_trie.insert('somebody1')
    test_trie.insert('somebody3')
    print(test_trie.contains("key"))
    print(test_trie.contains("somebody3"))
    print(test_trie.get_start("some"))
    print(test_trie.getSize())