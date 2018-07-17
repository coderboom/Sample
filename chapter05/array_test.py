# array,deque
# array:数组
import array

"""
array 和 list 的一个重要区别，array只能存放指定的数据类型,array性能高于list

    Type code   C Type             Minimum size in bytes 
            'b'         signed integer     1 
            'B'         unsigned integer   1 
            'u'         Unicode character  2  (see note) 
            'h'         signed integer     2 
            'H'         unsigned integer   2 
            'i'         signed integer     2 
            'I'         unsigned integer   2 
            'l'         signed integer     4 
            'L'         unsigned integer   4 
            'q'         signed integer     8  (see note) 
            'Q'         unsigned integer   8  (see note) 
            'f'         floating point     4 
            'd'         floating point     8 
"""

my_array = array.array('i')
my_array.append(1)
my_array.append('ad')  # error:an integer is required (got type str)
print(my_array)
