class Date():
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)

    # 静态方法不需要带self、cls这类型的参数，使用和普通方法类似
    @staticmethod
    def parse_from_string(date_string):
        year, month, day = tuple(date_string.split('-'))
        return Date(int(year), int(month), int(day))

    # cls指代当前类，self指代实例对象 ，当然cls、self都是可变的，她两不是关键字
    # 用类方法，返回的就是当前类的实例
    @classmethod
    def from_string(cls, date_string):
        year, month, day = tuple(date_string.split('-'))
        return cls(int(year), int(month), int(day))


if __name__ == '__main__':
    new_date = Date(2018, 10, 20)
    print(new_date)

    """
    实例方法只能被实例对象调用，静态方法(由@staticmethod装饰的方法)、类方法(由@classmethod装饰的方法)，
    可以被类或类的实例对象调用。
    """

    # 使用staticmethod方法,初始化对象
    # 劣势：编码的时候返回的类对象，当类改名时会对类的内部代码有影响
    date_str = "2018-20-1"
    new_date1 = Date.parse_from_string(date_str)
    print(new_date1)

    # 使用classmethod方法,初始化对象,用于不同的初始化类
    # 优势：编码的时候返回当前类的类对象，当类改名时会对类的内部代码没有影响
    date_str = "2018-20-11"
    new_date2 = Date.from_string(date_str)
    print(new_date2)
