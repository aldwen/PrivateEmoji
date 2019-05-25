class EmojisymblewithInfo:
    '''
    用于存放emoji符号和附属信息的类
    '''
    def __init__(self,symblechar,info中文名=None,info英文描述=None,info自定义短语=None):
        self.symblechar=symblechar
        self.info中文名=info中文名
        self.info英文描述=info英文描述

    def __repr__(self):
        return self.symblechar

    def add中文名(self,data):
        self.name中文=data

if __name__=="__main__":
    emojixiaolian=EmojisymblewithInfo('😵')
    print(emojixiaolian)
    print(emojixiaolian.info英文描述)
    print('end')


