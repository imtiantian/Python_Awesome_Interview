#!/usr/bin/env python
#-*-coding=utf-8-*-
#这是consistent hash(一致性哈希)的python实现方法,在分布式爬虫系统中判断新的URL是否真的可用

import md5
class HashRing(object):
    def __init__(self, nodes=None, replicas=3):
        """Manages a hash ring.
        `nodes` is a list of objects that have a proper __str__ representation.
        `replicas` indicates how many virtual points should be used pr. node,
        replicas are required to improve the distribution.
        """
        self.replicas = replicas
        self.ring = dict()
        self._sorted_keys = []
        if nodes:
            for node in nodes:
                self.add_node(node)
    def add_node(self, node):
        """Adds a `node` to the hash ring (including a number of replicas).
        """
        for i in xrange(0, self.replicas):
            key = self.gen_key('%s:%s' % (node, i))
            self.ring[key] = node
            self._sorted_keys.append(key)
        self._sorted_keys.sort()
    def remove_node(self, node):
        """Removes `node` from the hash ring and its replicas.
        """
        for i in xrange(0, self.replicas):
            key = self.gen_key('%s:%s' % (node, i))
            del self.ring[key]
            self._sorted_keys.remove(key)
    def get_node(self, string_key):
        """Given a string key a corresponding node in the hash ring is returned.
        If the hash ring is empty, `None` is returned.
        """
        return self.get_node_pos(string_key)[0]
    def get_node_pos(self, string_key):
        """Given a string key a corresponding node in the hash ring is returned
        along with it's position in the ring.
        If the hash ring is empty, (`None`, `None`) is returned.
        """
        if not self.ring:
            return None, None
        key = self.gen_key(string_key)
        nodes = self._sorted_keys
        for i in xrange(0, len(nodes)):
            node = nodes[i]
            if key &lt;= node:
                return self.ring[node], i
        return self.ring[nodes[0]], 0
    def get_nodes(self, string_key):
        """Given a string key it returns the nodes as a generator that can hold the key.
        The generator is never ending and iterates through the ring
        starting at the correct position.
        """
        if not self.ring:
            yield None, None
        node, pos = self.get_node_pos(string_key)
        for key in self._sorted_keys[pos:]:
            yield self.ring[key]
        while True:
            for key in self._sorted_keys:
                yield self.ring[key]
    def gen_key(self, key):
        """Given a string key it returns a long value,
        this long value represents a place on the hash ring.
        md5 is currently used because it mixes well.
        """
        m = md5.new()
        m.update(key)
        return long(m.hexdigest(), 16)

#其他实现方法
    # -*- coding: utf-8 -*-
    import hashlib

    class YHash(object):
        def __init__(self, nodes=None, n_number=3):
            """
            :param nodes:           所有的节点
            :param n_number:        一个节点对应多少个虚拟节点
            :return:
            """
            self._n_number = n_number  # 每一个节点对应多少个虚拟节点，这里默认是3个
            self._node_dict = dict()  # 用于将虚拟节点的hash值与node的对应关系
            self._sort_list = []  # 用于存放所有的虚拟节点的hash值，这里需要保持排序
            if nodes:
                for node in nodes:
                    self.add_node(node)

        def add_node(self, node):
            """
            添加node，首先要根据虚拟节点的数目，创建所有的虚拟节点，并将其与对应的node对应起来
            当然还需要将虚拟节点的hash值放到排序的里面
            这里在添加了节点之后，需要保持虚拟节点hash值的顺序
            :param node:
            :return:
            """
            for i in xrange(self._n_number):
                node_str = "%s%s" % (node, i)
                key = self._gen_key(node_str)
                self._node_dict[key] = node
                self._sort_list.append(key)
            self._sort_list.sort()

        def remove_node(self, node):
            """
            这里一个节点的退出，需要将这个节点的所有的虚拟节点都删除
            :param node:
            :return:
            """
            for i in xrange(self._n_number):
                node_str = "%s%s" % (node, i)
                key = self._gen_key(node_str)
                del self._node_dict[key]
                self._sort_list.remove(key)

        def get_node(self, key_str):
            """
            返回这个字符串应该对应的node，这里先求出字符串的hash值，然后找到第一个小于等于的虚拟节点，然后返回node
            如果hash值大于所有的节点，那么用第一个虚拟节点
            :param :
            :return:
            """
            if self._sort_list:
                key = self._gen_key(key_str)
                for node_key in self._sort_list:
                    if key <= node_key:
                        return self._node_dict[node_key]
                return self._node_dict[self._sort_list[0]]
            else:
                return None

        @staticmethod
        def _gen_key(key_str):
            """
            通过key，返回当前key的hash值，这里采用md5
            :param key:
            :return:
            """
            md5_str = hashlib.md5(key_str).hexdigest()
            return long(md5_str, 16)

    fjs = YHash(["127.0.0.1", "192.168.1.1"])
    print fjs.get_node("fjs32121")