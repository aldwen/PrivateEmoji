import json
import models
import os
path = os.getcwd()#获取当前路径
 
with open(path+r"\PrivateEmoji\src\aaa.json",encoding='utf-8') as load_f:
    load_dict = json.load(load_f)

ListofSymble=[]
for item in load_dict:
    symble=models.EmojisymblewithInfo(item['unicode'],info英文描述=item['aliases'])
    ListofSymble.append(symble)
for item in ListofSymble:
    print(item.symblechar+" ")    

#load_dict['smallberg'] = [8200,{1:[['Python',81],['shirt',300]]}]
#print(load_dict)

'''
with open(r"../config/record.json","w") as dump_f:
    json.dump(load_dict,dump_f)
'''