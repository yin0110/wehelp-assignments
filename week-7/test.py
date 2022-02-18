from crypt import methods
from email.policy import default
from webbrowser import get
from flask import Flask, url_for, redirect, session, jsonify
from flask import request
from flask import render_template
import mysql.connector
import yaml


# Static file 位置設定
app = Flask(__name__, static_folder="static", static_url_path="/")
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Back17658@@localhost/users"
app.secret_key = "2234"  # 設定session的密鑰

db = yaml.safe_load(open('secret.yaml'))
mydb = mysql.connector.connect(
    host=db["host"],
    user=db["user"],
    password=db["password"],
    database=db["db"]
)

cur = mydb.cursor(dictionary=True)
# 連接數據庫獲取游標，可以設置返回數據的格式（元組，命令元組，字典等）＝>這邊設置為返回字典
# 因此下面fectchone返回的會是字典


# 創建一個api引入我們的resource, endpoint為“／Hello”(跟class名字要一樣)


@app.route("/")
def index():
    if "signin" in session and not "":
        return redirect("/member")
    else:
        return render_template("login.html")  # css檔案要放到我們的後端連結裡，不然不能讀取


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        username = request.form["username"]
        password = request.form["password"]
        cur = mydb.cursor()
        cur.execute("SELECT * FROM members WHERE username = %s", (username,))
        account = cur.fetchone()
        if account:
            return redirect(url_for('error', message="alreadysigned"))
        else:
            cur.execute("INSERT INTO members(name, username, password) VALUES (%s, %s, %s)",
                        (name, username, password,))
            mydb.commit()
        return render_template("login.html")

    return render_template("login.html")


@app.route("/signin", methods=["POST"])
def signin():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # 注意 execute 後面要放的是 tuple 或是 dictionary，不能直接放 list
        cur.execute(
            'SELECT name, username, password FROM members WHERE username = %s AND password = %s', (username, password,))
        # 後面(username, password,)轉成tuple
        account = cur.fetchone()
        # fetone 出來的是tuple, 但因為前面有設置游標返回為字典，所以才資料類型才沒有問題，可以用字典方式取出
        if account:
            session["signin"] = True
            session["name"] = account["name"]
            session["username"] = account["username"]
            return redirect(url_for('loginok'))  # 這邊url要填function名稱
        else:
            return redirect(url_for('error', message="idpasswordwrong"))
    else:
        return render_template("login.html")
# 做這個是因為避免會員直接連到login裡但竟然是登入的，在未登入狀況必須把人轉出來


@app.route('/api/members', methods=["GET", "POST"])
def member():
    username = request.args.get("username")
    cur.execute(
        "SELECT id, name, username FROM members WHERE username=%s", (username,))
    userList = cur.fetchone()
    return jsonify({"data": userList})


@ app.route("/member", methods=["GET"])
def loginok():
    if "signin" in session and not "":
        name = session["name"]
        return render_template("loginok.html", user=name)
    # 回傳session的變數user給html使用
    else:
        return redirect("/")


@ app.route("/error")
def error():
    message = request.args.get("message")
    if message == "idpasswordblank":
        messagesToPage = "請輸入帳號、密碼"
        return render_template("loginblank.html", message=messagesToPage)
    # elif message == "blank":
    #     return render_template("loginblank.html")+'''
    #     <p>請輸入註冊訊息</p>
    #     '''
    elif message == "alreadysigned":
        messagesToPage = "帳號已經被註冊"
        return render_template("loginblank.html", message=messagesToPage)
    # 把message直接帶到前端，html用變數接回傳的文字

    else:
        messagesToPage = "帳號或密碼有誤"
        return render_template("loginblank.html", message=messagesToPage)


@ app.route("/signout")
def signout():
    session.pop("signin", None)
    session.pop("name", None)
    session.pop("username", None)
    return redirect("/")


app.run(port=3000, debug=True)
