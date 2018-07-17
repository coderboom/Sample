from collections import abc
import numbers


class Group:
    """
    支持切片操作
    """

    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])

    def __reversed__(self):
        #
        self.staffs.reverse()

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        # 使用if in 判断的时候会调用这个魔法函数
        if item in self.staffs:
            return True
        else:
            return False

    def __str__(self):
        return '员工有：' + '、'.join(self.staffs)


staffs = ['baby1', 'baby2', 'baby3', 'baby4']
group = Group(company_name='imocc', group_name='user', staffs=staffs)
# sub_group = group[0:2]
# print(sub_group)
# print(sub_group[1])

# if 'baby1' in group:
#     print('Yes')
#
# for staff in group:
#     print(staff)

reversed(group)  # 反转list(作用在原list上，反转其顺序)，会调用__reversed__方法，在__reversed__方法内需要调用reverse()方法
print(group)
print(staffs)
