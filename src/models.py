# -*- coding: UTF-8 -*-
import json

class EmojiInfo:
    '''
    用于存放emoji符号和附属信息的类
    '''
    def getUnicodeformEmoji(self,emojisymble):
        return hex(ord(emojisymble)).upper()

    def __init__(self,infoEmoji,infoUniCode=None,
                    info中文名=None,info英文描述=None,info输入串=None,
                    info标签=None,info别名=None,info附加信息=None,
                    info英文输入串=None):
        self.infoEmoji=infoEmoji
        if  infoUniCode==None:
            self.infoUniCode=self.getUnicodeformEmoji(infoEmoji[0])
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

def savetoSougou(filename,emlist,Default_Position=3):
    try:
        filename=open(filename,'w',encoding='utf-8')
        for symble in emlist:
            if symble.info输入串!=None:
                filename.write(symble.info输入串+','+repr(Default_Position)+'='+symble.infoEmoji+"\n")
        filename.close()
    except IOError:
        print("导出到 %S 时出错",filename)

class emlist:
    list=[]

    def addsymble(self,symble):
        if self.list==None: 
            raise ImportError #TODO:这里的错误类型需要修改

        if symble.infoEmoji not in [x.infoEmoji for x in self.list]:
            self.list.append(symble)
        else:
            for item in self.list:
                if symble.infoEmoji==item.infoEmoji:
                    if symble.infoUniCode!=None: item.infoUniCode=symble.infoUniCode
                    if symble.info输入串!=None: item.info输入串=symble.info输入串
                    print('这里需要 List 里的其他更新代码')
                    
    def LoadformXXL(self,filename):
        with open(filename,encoding='utf-8') as load_f:
            load_dict = json.load(load_f)

        self.list=[]
        for item in load_dict:
            symble=EmojiInfo(item['unicode'],
                info英文描述=",".join(item['aliases']),
                info标签=','.join(item['tags']),
                )
            self.list.append(symble)



if __name__=="__main__":
    emojixiaolian=EmojiInfo('⭐')
    print(emojixiaolian)
    print(emojixiaolian.info英文描述)
    print('end')


