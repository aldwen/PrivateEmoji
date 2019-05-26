class EmojisymblewithInfo:
    '''
    用于存放emoji符号和附属信息的类
    '''
    def __init__(self,infoEmoji,infoUniCode=None,
                    info中文名=None,info英文描述=None,info输入串=None,
                    info标签=None,info别名=None,info附加信息=None,
                    info英文输入串=None):
        self.infoEmoji=infoEmoji
        self.infoUniCode=infoUniCode
        self.info中文名=info中文名
        self.info英文描述=info英文描述
        self.info英文输入串=info英文输入串
        self.info输入串=info输入串
        self.info标签=info标签
        self.info别名=info别名
        self.info附加信息=info附加信息

 
    def __repr__(self):
        return self.infoEmoji

    def add中文名(self,data):
        self.info中文名=data

    

if __name__=="__main__":
    emojixiaolian=EmojisymblewithInfo('⭐')
    print(emojixiaolian)
    print(emojixiaolian.info英文描述)
    print('end')


