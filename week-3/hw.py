# 要求一

import urllib.request as re
import json
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with re.urlopen(src) as feedback:
    data1 = json.load(feedback)
plist = data1["result"]["results"]
with open("data.csv", mode="w", encoding="utf-8") as file:
    for p in plist:
        p1 = p["file"]
        x = p1.split("https://")  # 將圖片資訊切分開來
        y = "https://"+x[1]
        file.write(p["stitle"]+","+p["address"][5:8] +
                   ","+p["longitude"]+","+p["latitude"]+","+y+"\n")  # +\n每一個資訊分行
