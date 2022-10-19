from flask import Flask # 載入 Flask
from flask import request # 載入 Request 物件
from flask import render_template # 載入 render_template
from flask import redirect
from flask import url_for
from flask import session
import os # 產生 session 亂數密鑰
# 建立 Application 物件，可以設定靜態檔案的路徑處理
# 所有在 public 資料夾底下的檔案，都對應到網址路徑 /檔案名稱
week4_hw4=Flask(
    __name__,
    static_folder="static", # 靜態檔案的資料夾名稱
    static_url_path="/" # 靜態檔案對應的網址名稱
)

week4_hw4.secret_key=os.urandom(12).hex() # 設定 Session 的密鑰，才能開始使用!!

# 使用 GET 方法，處理路徑 / 的對應函式
@week4_hw4.route("/", methods=["GET"])
def home(): # 用來回應路徑 / 的對應函式
    session["user-status"]="未登入"
    return render_template("calculate.html")
    # return render_template("home.html")

# 使用 POST　方法，處理路徑 /signin 的對應函式
@week4_hw4.route("/signin", methods=["POST"])
def signin():
    # 接收 GET 方法的 Query String　
    # maxNumber=request.args.get("max", "")
    # 接收 POST 方法的 Query String
    account=request.form["account"]
    password=request.form["password"]
    # 要注意 logical operators 運用 and 及 or 時兩個變數都要寫判斷式
    # redirect 中的 code=302(307) 時為 GET(POST) 方法。
    if account=="test" and password=="test":
        session["user-status"]="已登入"
        print(session["user-status"])
        return redirect(url_for('member')) 
    elif account=="" or password=="": # url_for('要去的地方', 變數名稱='夾帶資訊')
        return redirect(url_for('error', message='請輸入帳號、密碼'))
    elif account!="test" or password!="test":
        return redirect(url_for('error', message='帳號、或密碼輸入錯誤'))


# 處理路徑 /member 的對應函式
@week4_hw4.route("/member")
def member():
    if session["user-status"] == "未登入":
        return redirect("/")
    return render_template("status.html", header="歡迎光臨，這是會員頁", login_infor="恭喜您，成功登入系統", signout="登出系統")

# 處理路徑 /error 的對應函式
@week4_hw4.route("/error")
def error():
    infor=request.args.get("message", "") # 去索取 for_url 中變數名稱所夾帶的訊息
    return render_template("status.html", header="失敗頁面", login_infor=infor)

# 處理路徑 /signout 的對應函式
@week4_hw4.route("/signout")
def signout():
    session["user-status"]="未登入"
    print(session["user-status"])
    return redirect("/")

# 處理路徑 /square 的對應函式
@week4_hw4.route("/square", methods=["GET", "POST"])
def square():
    num=request.form["calculate"]
    return redirect(url_for('square_2', targetNum=num))

# 處理路徑 /square/ 的對應函式
@week4_hw4.route("/square/<targetNum>")
def square_2(targetNum):
    num=int(targetNum)**2
    return render_template("status.html",header="正整數平方計算結果", login_infor=num)

# 啟動網站伺服器，可透過 port 參數指定埠號
week4_hw4.run(port=3000)