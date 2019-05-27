import json
import models

def InitFromXXLEmoji(filename):
    with open(filename,encoding='utf-8') as load_f:
        load_dict = json.load(load_f)

    ListofSymble=[]
    for item in load_dict:
        symble=models.EmojisymblewithInfo(item['unicode'],
            info英文描述=",".join(item['aliases']),
            info标签=','.join(item['tags']),
            )
        ListofSymble.append(symble)

    return ListofSymble
    
if __name__=="__main__":

    filename=r"D:\Aldwen\Coding\Python\PrivateEmoji\PrivateEmoji\resources\xxl-emoji.json"
    getlist=InitFromXXLEmoji(filename)

    for item in getlist:
        print(item.infoEmoji)

