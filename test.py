# import time
# print(time.time())
# a = "2013-10-10 23:40:00"
# print(a.split(" ")[1])
# timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
# #轉換為時間戳:
# timeStamp = int(time.mktime(timeArray))
# print(timeStamp)
# timeStamp == 1381419600

import re

absdate_pattern = r"(ad )+([0-9]*)+(-)+([0-9]*)+(-)+[0-9]*"
a = "ad 2020-18-80 0"
print(re.fullmatch(absdate_pattern,a))

c = "012"

# #載入requests套件
import requests
#需要載入os套件，可處理文件和目錄
import os
#創建目錄
os.makedirs('./img/',exist_ok=True)
url='圖片網址'
r=requests.get("https://i.pixiv.cat/img-master/img/2020/12/13/15/32/26/86274118_p0_master1200.jpg")
with open('./img/圖片名稱','wb') as f:
#將圖片下載下來
    f.write(r.content)

import zipfile
with zipfile.ZipFile('./img/archive.zip', 'w') as zf:
    zf.write('./img/1.jpg')
    zf.write('./img/2.jpg')
