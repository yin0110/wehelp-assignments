import os
from crypt import methods
from email.policy import default
from webbrowser import get
from flask import Flask, url_for, redirect, session
from flask import request
from flask import render_template
import mysql.connector
import pymysql


# Static file 位置設定
app = Flask(__name__, static_folder="static", static_url_path="/")
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Back17658@@localhost/users"
app.secret_key = "2234"  # 設定session的密鑰
bd_password = os.environ.get('DB_PASSWORD')
mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="qazxsw123",
    database="users",
    cursorclass=pymysql.cursors.DictCursor
)

cur = mydb.cursor()


@app.route("/")
def index():
    if "signin" in session and not "":
        # if session["status"] == "已登入":
        return redirect("/member")
    else:
        return render_template("login.html")  # css檔案要放到我們的後端連結裡，不然不能讀取


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST" and "username" in request.form and "password" in request.form and "name" in request.form:
        name = request.form["name"]
        username = request.form["username"]
        password = request.form["password"]
        cur = mydb.cursor()
        cur.execute("SELECT * FROM members WHERE username = %s", (username,))
        account = cur.fetchone()
        if account:
            return redirect(url_for('error', message="alreadysigned"))
        else:
            # sql = "INSERT INTO members(name, username, password) VALUES ('%s', '%s', '%s')"
            # cur.execute(sql)
            # cur.execute("INSERT INTO members VALUES (%s, %s, %s)")
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
        # cur.execute(
        # 'SELECT * FROM members WHERE username= %s AND password= %s', (username, password,))
        # cur.execute(
        #     "SELECT * FROM members WHERE (username, password) VALUES (%s, %s,)" % (
        #         username, password,))
        cur.execute(
            'SELECT name, username, password FROM members WHERE username = %s AND password = %s', (username, password,))
        # sql = "SELECT * FROM members WHERE (username, password) VALUES (%s, %s)"
        # val = (username, password,)
        # cur.execute(sql, val,)
        account = cur.fetchone()
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


@ app.route("/member", methods=["GET"])
def loginok():
    # if session["status"] == "已登入":
    if "signin" in session and not "":
        name = session["name"]
        return render_template("loginok.html")+'''
        <div class="login">
        恭喜'''+name+'''，成功登入系統<br/>'''+'''
        <a href="/signout">登出系統</a>
        </div>
        '''
    else:
        return redirect("/")


@ app.route("/error")
def error():
    message = request.args.get("message")
    if message == "idpasswordblank":
        return render_template("loginblank.html")+'''
        <p>請輸入帳號、密碼</p>
        '''
    elif message == "blank":
        return render_template("loginblank.html")+'''
        <p>請輸入註冊訊息</p>
        '''
    elif message == "alreadysigned":
        return render_template("loginblank.html")+'''
        <p>帳號已經被註冊</p>
        '''
    else:
        return render_template("loginfail.html")+'''
        <p>帳號或密碼有誤</p>
        '''


@ app.route("/signout")
def signout():
    session.pop("signin", None)
    session.pop("name", None)
    session.pop("username", None)
    # session["status"] = "未登入"
    return redirect("/")


app.run(port=5000)
