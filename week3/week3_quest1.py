# 景點名稱("stitle"),區域("address"),經度("longitude")
# ,緯度("latitude"),第一張圖檔網址("file")
# 串接, 擷取公開資料
import urllib.request as req
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with req.urlopen(src) as response:
    data=json.load(response) # 利用 json 讀取 json 資料格式

# 依序取得景點名稱("stitle"),區域("address"),經度("longitude"),緯度("latitude"),第一張圖檔網址("file")
data_pool=data["result"]["results"] # 整個 data 池
# 底下的 2 行 code 是把北投區拉出來的單獨測試(成功!!)
# test=data_pool[0]["address"]
# print(test[5:8])

#底下為把第一張img 拉出來的測試區(成功!! 使用 .split("以該字串為分界劃分為左右")[串列排序]
# for i in range(3):
#     img=data_pool[i]["file"]
#     print("這裡這裡:", "https:"+img.split("https:")[1])

#底下為測試單一檔案是否為2015年後(成功!)
# print(type(data_pool[0]["xpostDate"]))
# if int(data_pool[0]["xpostDate"][0:4]) >= 2015:
#     print("yes")

with open("data.csv", "w", encoding="utf-8") as file: # 實務最佳範例
    for data in data_pool:
        if int(data["xpostDate"][0:4]) >= 2015: # 只要2015年以後的資料
            address=data["address"][5:8] # 可以觀察到每一個 address 都是 臺北市+ " "+ OO區XXXXX，OO區是目標!
            data=(data["stitle"], address, data["latitude"], "https:"+data["file"].split("https:")[1]) # 產生一個 tuple
            result=",".join(data) # 將 tuple 轉換成 str
            file.write(result+"\n") # 將 file 寫入 data.csv 檔案中，注意! file.write 只能輸出 str


