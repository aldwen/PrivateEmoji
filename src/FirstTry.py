# -*- coding: UTF-8 -*-

import models
import pickle

try:
    pkl_file=open(r'.\PrivateEmoji\resources\mylist.pkl','rb')
    a_emojiList=pickle.load(pkl_file)
    pkl_file.close()
    print('Load data form PKL file')
except IOError:
    a_emojiList=models.EmojiInfoList()
    a_emojiList.LoadformXXL(r".\PrivateEmoji\resources\xxl-emoji.json")
    print("Load data from JSON file") 


aaa=models.EmojiInfo('⭐',info中文名='星星',info输入串='xingxing')
a_emojiList.addsymble(aaa)

bbb=models.EmojiInfo('🌹',info中文名='玫瑰',info输入串='meigui')
a_emojiList.addsymble(bbb)

for symble in a_emojiList.list:
    print(symble,end=' ')

pkl_file=open(r'.\PrivateEmoji\resources\mylist.pkl','wb')
pickle.dump(a_emojiList,pkl_file)
pkl_file.close()

models.savetoSougou(r'.\PrivateEmoji\resources\sougou.txt',a_emojiList.list)
