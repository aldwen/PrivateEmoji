# -*- coding: UTF-8 -*-

import models
import pickle

emojidict=[]


try:
    savefile=open('mylist.pkl','rb')
    emojidict=pickle.load(savefile)
    savefile.close()
except IOError:
    print("File is not accessible.") 

aaa=models.EmojisymblewithInfo('⭐',info中文名='星星',info输入串='xingxing',symbleunicode= u'\U0001F947')
if aaa.symblechar not in [x.symblechar for x in emojidict]:
    emojidict.append(aaa)

bbb=models.EmojisymblewithInfo('🌹',info中文名='玫瑰',info输入串='meigui',symbleunicode=u'\U0001F170')
if bbb.symblechar not in [x.symblechar for x in emojidict]:
    emojidict.append(bbb)

for symble in emojidict:
    print(symble)

savefile=open('mylist.pkl','wb')
pickle.dump(emojidict,savefile)
savefile.close()

_DEFAULT_POSITION = 3
def savetoSougou(filename,EmojiDict,Default_Position=3):
    try:
        filename=open(filename,'w',encoding='utf-8')
        for symble in EmojiDict:
            filename.write(symble.info输入串+','+repr(Default_Position)+'='+symble.symblechar+"\n")
        filename.close()
    except IOError:
        print("导出到 %S 时出错",filename)

savetoSougou('sougou.txt',emojidict,_DEFAULT_POSITION)
