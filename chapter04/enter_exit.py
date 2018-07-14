# with open('html.html', 'w') as f:
#     pass
"""
上下文管理器
    可以自己实现，实现__enter__和__exit__这两个魔法函数即可，
    通过with语句使用上下文管理器的时候，
    ----先通过__enter__进入一个运行时上下文，并在代码块结束后退出上下文（即执行__exit__函数）
"""

import time


class MyTimer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()
        print('开始时间：', self.start)
        return self

    def __exit__(self, *unused):
        self.end = time.time()
        print('结束时间：', self.end)
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000
        if self.verbose:
            print("elapsed time: %f ms" % self.msecs)

    def doing(self):
        print('11111111111111111')


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


with MyTimer(True) as f:
    print(fib(30))
    f.doing()
    