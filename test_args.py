#-* -coding:GBK -* -
#����ע��ģ��
def func(id, i=1,*args, sex = '��', **kwargs):
    """
    Python2
    ��Python2�У�Cѡ���Ǵ�ģ���Ϊa=1��������Ĭ�ϲ�������Ĭ�ϲ���ֻ���ڿɱ����֮ǰ
    Python����˳�򣺱�ѡ������Ĭ�ϲ������ɱ�����͹ؼ��ֲ�����

    Python3
    ��python3�У�Cѡ���ǶԵģ���Ϊa=1�������������ؼ��ֲ������������ؼ��ֲ�����Ҫ�ڿɱ����֮��

    Python3����˳�򣺱�ѡ������Ĭ�ϲ������ɱ�����������ؼ��ֲ����͹ؼ��ֲ�����
    """
    print(id)
    print(i)
    print(sex)
    print(args)
    print(kwargs)

func('a',0,'b','c', sex='��', name='allen',age=22)