# -*- coding: UTF-8 -*-
import json

'''
    这个版本里，emojiinfo 表示为字典，不用类
    {''}
'''


#  class EmojiInfo:
#     '''
#     用于存放emoji符号和附属信息的类
#     '''
#     def getUnicodeformEmoji(self,unicode):
#         return hex(ord(unicode)).upper()
    
#     def getEmojifromUnicode(self,infoUnicode):
#         return chr(int(infoUnicode,16))

#     def __init__(self,unicode,infoUniCode=None,
#                     info中文名=None,info英文描述=None,info输入串=None,
#                     info标签=None,info别名=None,info附加信息=None,
#                     info英文输入串=None):

#         self.unicode=unicode
#         if  infoUniCode==None:
#             self.infoUniCode=self.getUnicodeformEmoji(unicode[0])
#         '''
#         初始化时以unicode为准还是 emoji图形为准，这是个问题
#         self.infoUniCode=infoUniCode
#         if  unicode==None:
#             self.unicode=self.getEmojifromUnicode(infoUniCode)
#         '''
#         self.info中文名=info中文名
#         self.info英文描述=info英文描述
#         self.info英文输入串=info英文输入串
#         self.info输入串=info输入串
#         self.info标签=info标签
#         self.info别名=info别名
#         self.info附加信息=info附加信息
 
#     def __repr__(self):
#         return self.unicode

#     def add中文名(self,data):
#         self.info中文名=data

# def getdictfromEmoji(emojiinfo):
#     return {'unicode':emojiinfo.unicode,
#             'infoUnicode':emojiinfo.infoUniCode,
#             'info输入串':emojiinfo.info输入串
#     }


class emlist:
    _list=[]

    def addsymble(self,symble):
        if self._list==None: 
            raise ImportError #TODO:这里的错误类型需要修改
        for item in self._list:
            if symble['unicode']==item['unicode']:
                item.update(symble)
        else:
            self._list.append(symble)


    def LoadformXXL(self,filename):
        with open(filename,encoding='utf-8') as load_f:
            self._list = json.load(load_f)
        
       
    
    def SavetoJson(self,filename):
        with open(filename, "w", encoding='utf-8') as fw:
            fw.write(json.dumps(self._list, indent=4))
        
    def savetoSougou(self,filename,Default_Position=3):
        try:
            filename=open(filename,'w',encoding='utf-8')
            for symble in self._list:
                if 'info输入串' in  symble.keys():
                    filename.write(symble['info输入串']+','+repr(Default_Position)+'='+symble['unicode']+"\n")
            filename.close()
        except IOError:
            print("导出到 %S 时出错",filename)


if __name__=="__main__":
    
    import models
    a_emojiList=emlist()
    a_emojiList.LoadformXXL(r"..\resources\xxl-emoji.json")
    print("Load data from JSON file") 


    aaa={'unicode':'⭐','info中文名':'星星','info输入串':'xingxing'}
    a_emojiList.addsymble(aaa)

    bbb={'unicode':'🌹','info中文名':'玫瑰','info输入串':'meigui'}
    a_emojiList.addsymble(bbb)

    ccc={'unicode':'😄','info输入串':'xiaolian','info中文名':'笑脸'}
    a_emojiList.addsymble(ccc)

    for symble in a_emojiList._list:
        print(symble,end=' ')


    a_emojiList.SavetoJson(r'..\temp\myjson.json')

    a_emojiList.savetoSougou(r'..\temp\sougou.txt',Default_Position=2)

