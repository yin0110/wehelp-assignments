from crypt import methods
from webbrowser import get
from flask import Flask, url_for, redirect, session
from flask import request
from flask import render_template
# Static file 位置設定
app = Flask(__name__, static_folder="static", static_url_path="/")
app.secret_key = "2234"  # 設定session的密鑰


@app.route("/")
def index():
    if session["status"] == "已登入":
        return redirect("/member")
    else:
        return render_template("login.html")  # css檔案要放到我們的後端連結裡，不然不能讀取


@app.route("/signin", methods=["POST"])
def signin():
    idname = request.form["inputId"]
    password = request.form["inputPassword"]
    if idname == "test" and password == "test":
        session["status"] = "已登入"
        return redirect(url_for('loginok'))  # 這邊url要填function名稱
    elif idname == "" or password == "":
        return redirect(url_for('error', message="idpasswordblank"))
    else:
        return redirect(url_for('error', message="idpasswordwrong"))


@app.route("/member")
def loginok():
    if session["status"] == "已登入":
        return render_template("loginok.html")
    else:
        return redirect("/")


@app.route("/error")
def error():
    message = request.args.get("message")
    if message == "idpasswordblank":
        return render_template("loginblank.html")
    else:
        return render_template("loginfail.html")


@app.route("/signout")
def signout():
    session["status"] = "未登入"
    return redirect("/")


app.run(port=3000)
