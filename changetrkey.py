import os
from upload_machine.utils.edittorrent.edittorrent import *
path1 = r'C:\Users\moyu\AppData\Local\transmission\Torrents'
ls = os.listdir(path1)
num=0
for i in ls:
    c_path=os.path.join(path1,i)
    if os.path.splitext(i)[1].lower()=='.torrent':
        num=num+1
        print(num)
        t=Torrent()
        t.load(c_path)
        if  b'azusa.ru' in t.data[b"announce"]:
            t.data[b"announce"]=t.data[b"announce"].replace(b'azusa.ru',b'tracker.azusa.wiki')
            t.dump(c_path)