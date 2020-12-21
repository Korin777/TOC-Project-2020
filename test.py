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