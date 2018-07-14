# 两种应用场景
# 1、检查一个类是否有某种方法


class Company(object):
    def __init__(self, emloyee_list):
        self.emloyee = emloyee_list

    def __len__(self):
        return len(self.emloyee)


com = Company(['baby1', 'baby2'])
print(hasattr(com, '__len__'))  # hasattr 判断com中是否含有__len__方法
print(len(com))

"""
在某种情况下需要判断某个对象的类型
"""
from collections.abc import Sized

# ------------------------------------------------------------------
"""
2 强制某个子类必须实现某些方法
比如实现一个web框架，继承cache（redis，cache等），需要设计一个抽象基类，指定子类必须实现某些方法

"""

# 简单的方法，通过抛出NotImpementedError
# class CacheBase():
#     def get(self, key):
#         raise NotImplementedError
#
#     def set(self, key, value):
#         raise NotImplementedError


# class RedisCache(CacheBase):
#     pass


# redis_cache = RedisCache()
# redis_cache.set('key', 'value')


"""
"""
# 通过abc 实现抽象基类,在初始化的时候便会抛出异常
import abc


class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


class RedisCache(CacheBase):
    pass


redis_cache = RedisCache()
redis_cache.set('key', 'value')
