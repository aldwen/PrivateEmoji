# -*- coding: UTF-8 -*-

import models
import pickle

'''
changepath=1
if changepath==1:
    paths=r'..\\'
elif changepath==2:
    paths=r'.\\PrivateEmoji\\'
'''

try:
    pkl_file=open(r'..\temp\mylist.pkl','rb')
    a_emojiList=pickle.load(pkl_file)
    pkl_file.close()
    print('Load data form PKL file')
except IOError:
    a_emojiList=models.emlist()
    a_emojiList.LoadformXXL(r"..\resources\xxl-emoji.json")
    print("Load data from JSON file") 


aaa=models.EmojiInfo('⭐',info中文名='星星',info输入串='xingxing')
a_emojiList.addsymble(aaa)

bbb=models.EmojiInfo('🌹',info中文名='玫瑰',info输入串='meigui')
a_emojiList.addsymble(bbb)

for symble in a_emojiList.list:
    print(symble,end=' ')

pkl_file=open(r'..\temp\mylist.pkl','wb')
pickle.dump(a_emojiList,pkl_file)
pkl_file.close()

a_emojiList.SavetoJson(r'..\temp\myjson.json')

models.savetoSougou(r'..\temp\sougou.txt',a_emojiList.list,Default_Position=2)
