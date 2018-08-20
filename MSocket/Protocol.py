#-*- coding:utf-8 _*-
"""
@author:hql
@file: Protocol
@time: 2018/08/{DAY}
"""
import pickle
import datetime
_MSG_TEM = """
            'HEAD':%s,
            'DATA':%s,
            'FROM':%s,
            'TO':%s,
            'TIME':%s,
            """


class Protocol:
    __doc__="""
        'HEAD':%s,type of stream e.g. text,file,dict,list,order
        'DATA':%s,data ,such as str list dict or data class you def
        'FROM':%s,who send
        'TO':%s,send to
        'TIME':%s,now time h:m:s
    """
    orders = {}

    def __init__(self):
        self.bind('login',self.login)
        self.bind('text',print)

    def pack(self,data,_from,_to,head="text"):
        MSG_TEM = {}
        ti = datetime.datetime.now().strftime("%T")
        strdata = pickle.dumps(data)

        MSG_TEM['DATA'] = strdata
        MSG_TEM['FROM'] = _from
        MSG_TEM['TO'] = _to
        MSG_TEM['TIME'] = ti
        MSG_TEM['HEAD'] = head
        package = pickle.dumps(MSG_TEM)
        return package

    def unpack(self,package):
        MSG_TEM = pickle.loads(package)
        MSG_TEM['DATA'] = pickle.loads(MSG_TEM['DATA'])
        return MSG_TEM

    def interpret_msg(self,msg ):
        head = msg['HEAD']
        if head not in self.orders.keys():
            print("未知指令")
            return False,"未知指令"
        else:
            return self.orders[head](msg)

    def bind(self,order,call):
        self.orders.update({order:call})

    def login(self,args):
        args = args['DATA']
        print(f"LOGIN:\n\tusr:{args['usr']}\n\tpassword:{args['password']}")
        return True,"登陆成功"



if __name__ == "__main__":
    p = Protocol()
    ps = p.pack({'usr':"123",'password':"123"},1,2,'login')
    print(ps)
    d = p.unpack(ps)
    p.interpret_msg(d)