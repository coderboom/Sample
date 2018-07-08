class Company(object):
    def __init__(self, emloyee_list):
        self.emloyee = emloyee_list

    def __str__(self):  # 对字符串需要格式化的时候调用
        return ','.join(self.emloyee)

    def __repr__(self):  # 开发模式下，和__str__ 一样，格式化字符串
        return ','.join(self.emloyee)

    def __getitem__(self, item):
        return self.emloyee[item]

    def __len__(self):
        return self.emloyee.__len__()


company = Company(['tom', 'bob', 'jane'])
print(company)  # tom,bob,jane
company  # tom,bob,jane
print(len(company))
