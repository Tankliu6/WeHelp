from flask import Flask # 載入 Flask
from flask import request # 載入 Request 物件
from flask import render_template # 載入 render_template
from flask import redirect
from flask import url_for
from flask import session
import os # 產生 session 亂數密鑰
import mysql.connector # 連接 python 與 mysql 資料庫
from mySQL import getPassword # 隱藏 password 的方法
# 連線(connection)到資料庫
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password=getPassword(),
    database="website"
)
# 創造一台往返資料庫與後端的搬運卡車(cursor();)
mycursor = mydb.cursor()

# 建立 Application 物件，可以設定靜態檔案的路徑處理
# 所有在 static 資料夾底下的檔案，都對應到網址路徑 /檔案名稱
week6=Flask(
    __name__,
    static_folder="static", # 靜態檔案的資料夾名稱
    static_url_path="/" # 靜態檔案對應的網址名稱
)

week6.secret_key=os.urandom(12).hex() # 設定 Session 的密鑰，才能開始使用!!

# 使用 GET 方法，處理路徑 / 的對應函式
@week6.route("/", methods=["GET"])
def home(): # 用來回應路徑 / 的對應函式
    session["user-status"] = {}
    print(session)
    return render_template("calculate_jsmethod.html")

# 使用 POST　方法，處理路徑 /signin 的對應函式
@week6.route("/signin", methods=["POST"])
def signin():
    # 接收 GET 方法的 Query String　
    # maxNumber=request.args.get("max", "")
    # 接收 POST 方法的 Query String
    username=request.form["username"]
    password=request.form["password"]
    sql = "SELECT id, name, username, password FROM member WHERE username=%s" # SQL 指令
    value = (username, ) # 與後端程式互動的變數
    mycursor.execute(sql, value) # 卡車執行，前往資料執行 SQL 指令
    myresult=mycursor.fetchall() # fetchall()將所有資料取出
    if username=="" or password=="":
        return redirect(url_for('error', message='請輸入帳號、密碼'))
    elif username == myresult[0][2] and password == myresult[0][3]:
        session.update({
            "id":myresult[0][0],
            "name":myresult[0][1],
            "username":myresult[0][2],
            "password":myresult[0][3],
            "user-status":"已登入"
        })
        return redirect("/member")
    else:
        return redirect(url_for('error', message='帳號、或密碼輸入錯誤'))
    # 要注意 logical operators 運用 and 及 or 時兩個變數都要寫判斷式
    # redirect 中的 code=302(307) 時為 GET(POST) 方法。


# 處理路徑 /member 的對應函式
@week6.route("/member")
def member():
    print(session)
    if session["user-status"] != "已登入":
        return redirect("/")
    #使用 INNER JOIN 透過外鍵 member_id 取出 message 資料表中留言者的名字(name)及對應的留言(content)
    name=session["name"]
    mycursor.execute("SELECT member.name, message.content FROM member INNER JOIN message ON member.id = message.member_id")
    myNameContent=mycursor.fetchall()
    return render_template(
        "member.html", 
        header="歡迎光臨，這是會員頁", 
        login_infor=f"{name}，歡迎登入系統", 
        signout="登出系統", 
        come_message="快來留言吧",
        content=myNameContent
    )
    
# 處理路徑 /message 的對應函式
@week6.route("/message", methods=["POST", "GET"]) # 直接輸入 url 訪問 127.0.0.1:3000/message 時會以 GET 方法訪問
def message():
    if session["user-status"] != "已登入": # 防止非會員進入
        redirect("/")
    if request.method == "POST":
        content=request.form["message"]
        id=int(session["id"]) # 存放在 cookie 的 id
        sql=("INSERT INTO message (member_id, content) VALUES(%s, %s)") # 將資料放進留言表當中
        value=(id, content)
        mycursor.execute(sql, value)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.") # 會員輸入內容，確認放進留言資料表中
        return redirect("/member")
    return redirect("/") # 防止url直接進入此網頁

# 處理路徑 /error 的對應函式
@week6.route("/error")
def error():
    infor=request.args.get("message", "") # 去索取 for_url 中變數名稱所夾帶的訊息
    return render_template("status.html", header="失敗頁面", login_infor=infor)

# 處理路徑 /signout 的對應函式
@week6.route("/signout")
def signout():
    session.clear()
    session.update({
        "user-status":"未登入"
    })
    return redirect("/")

# 處理路徑 /signup 的對應函式
@week6.route("/signup", methods=["POST"])
def signup():
    # 從瀏覽器以 POST 方法接收註冊時的 姓名、帳號、密碼
    name=request.form["name"]
    username=request.form["username-signUp"]
    password=request.form["password-signUp"]
    sql = "SELECT username FROM member WHERE username = %s"
    value = (username, )
    mycursor.execute(sql, value)
    myresult=mycursor.fetchall() # 卸下卡車(cursor)上的資料，指定給 myresult
    # 確認新註冊的 username 是否已經在資料庫(database)當中
    if name == "" or username == "" or password == "": # 姓名、帳號、密碼，留白時會出現無效註冊
        return render_template("status.html", header="失敗頁面", login_infor="無效註冊")
    elif username in myresult:
        return render_template("status.html", header="失敗頁面", login_infor="帳號已經被註冊")
    elif username not in myresult:
        sql = "INSERT INTO member(name, username, password) VALUES (%s, %s, %s)" 
        value = (name, username, password)
        mycursor.execute(sql, value) # 卡車裝載指令 sql, 及%s所用的值 
        mydb.commit() # 
        print(mycursor.rowcount, "record inserted.")
        return redirect("/")
# 啟動網站伺服器，可透過 port 參數指定埠號
week6.run(port=3000)