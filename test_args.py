#-* -coding:GBK -* -
#中文注释模板
def func(id, i=1,*args, sex = '男', **kwargs):
    """
    Python2
    在Python2中，C选项是错的，因为a=1被当做了默认参数，而默认参数只能在可变参数之前
    Python参数顺序：必选参数、默认参数、可变参数和关键字参数。

    Python3
    在python3中，C选项是对的，因为a=1被当做了命名关键字参数，而命名关键字参数需要在可变参数之后

    Python3参数顺序：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
    """
    print(id)
    print(i)
    print(sex)
    print(args)
    print(kwargs)

func('a',0,'b','c', sex='男', name='allen',age=22)