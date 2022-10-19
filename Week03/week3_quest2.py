# 抓取 PPT 電影版的網頁原始碼 (HTML)
import urllib.request as req
# 抓取單一頁面的方程式
good=[]; normal=[]; weird=[] 
def getData(url):
    # 建立一個 Request 物件，附加 Request Headers 的資訊，目的是為了將自己偽裝成一般使用者
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"  
    })
    with req.urlopen(request) as response:  # 與一般不同的是不直接放入 url 而是換成另外建立的 request 物件
        data_pool=response.read().decode("utf-8")

    # 解析原始碼， 取得每篇文章的標題
    # 使用 beautifulsoup4； 安裝方式:pip install beautifulsoup4
    import bs4
    root=bs4.BeautifulSoup(data_pool, "html.parser") # 讓 BeautifulSoup 協助我們解析 HTML 格式文件
    titles_all=root.find_all("div", class_="title") # 尋找所有 class="title" 的 div 標籤    
    for title in titles_all:
        if title.a !=None: # 如果標題包含 a 標籤 (沒有被刪除)， 印出來
            if title.a.string[0:4] == "[好雷]": # 如果標題前4個字包含[負雷]、[普雷]、[好雷]，印出來
                good.append(title.a.string)
                #print(title.a.string)
            if title.a.string[0:4] == "[普雷]":
                normal.append(title.a.string)
                #print(title.a.string)
            if title.a.string[0:4] == "[負雷]":
                weird.append(title.a.string)
                #print(title.a.string)
    # 抓取上一頁的連結(為了抓取多個頁面的準備)
    nextLink=root.find("a", string="‹ 上頁") # 找到內文是 ‹ 上頁 的 a 標籤
    return nextLink["href"] # 抓取這個標籤中的 href 屬性，並傳出 function 外

# 主程序: 抓取多個頁面的標題
pageURL="https://www.ptt.cc/bbs/movie/index.html"
count=0
while count<10:
    pageURL="https://www.ptt.cc"+getData(pageURL) #記得 getData(pageURL) 會先呼叫一次第一頁再進下一輪
    count+=1

# print(good);  print(normal); print(weird)
list_titles_all=good+normal+weird
#print(titles_all)
#
with open("movie.txt", "w", encoding="utf-8") as file: # 實務最佳範例
    for title in list_titles_all:
        file.write(title+"\n") # 將 file 寫入 movie.txt 檔案中，注意! file.write 只能輸出 str
#