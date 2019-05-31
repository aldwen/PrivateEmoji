# -*- coding: UTF-8 -*-

import models
import pickle

changepath=2
if changepath==1:
    paths=r'..\\'
elif changepath==2:
    paths=r'.\\PrivateEmoji\\'

try:
    pkl_file=open(paths+r'temp\mylist.pkl','rb')
    a_emojiList=pickle.load(pkl_file)
    pkl_file.close()
    print('Load data form PKL file')
except IOError:
    a_emojiList=models.emlist()
    a_emojiList.LoadformXXL(paths+r"resources\xxl-emoji.json")
    print("Load data from JSON file") 


aaa=models.EmojiInfo('⭐',info中文名='星星',info输入串='xingxing')
a_emojiList.addsymble(aaa)

bbb=models.EmojiInfo('🌹',info中文名='玫瑰',info输入串='meigui')
a_emojiList.addsymble(bbb)

for symble in a_emojiList.list:
    print(symble,end=' ')

pkl_file=open(r'.\PrivateEmoji\temp\mylist.pkl','wb')
pickle.dump(a_emojiList,pkl_file)
pkl_file.close()

a_emojiList.SavetoJson(r'.\PrivateEmoji\temp\myjson.json')

models.savetoSougou(r'.\PrivateEmoji\temp\sougou.txt',a_emojiList.list,Default_Position=2)
