import json
import models
import os
path = os.getcwd()#获取当前路径
 
with open(path+r"\PrivateEmoji\resources\xxl-emoji.json",encoding='utf-8') as load_f:
    load_dict = json.load(load_f)

ListofSymble=[]
ListofSymble2=[]

for item in load_dict:
    ListofSymble2.append{'infoEmoji':item['unicode']}

    symble=models.EmojisymblewithInfo(item['unicode'],
            info英文描述=",".join(item['aliases']),
            info标签=','.join(item['tags']),
            )
    ListofSymble.append(symble)


'''with open(r"./PrivateEmoji/resources/EmojiClass.json","w",encoding='utf-8') as dump_f:
    json.dump(ListofSymble,dump_f)
'''
print('End of Init Data')