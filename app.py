from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        print(request.form)
        user = request.form.get("user")
        hobby = request.form.getlist("hobby")
        print(user, hobby)
        return "注册成功"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        print(request.form)
        user = request.form.get("user")
        password = request.form.get("pwd")
        print(user, password)
        return "登录成功"


@app.route("/home", methods=["GET"])
def home():
    return render_template("/home.html")
# @app.route('/get/reg', methods=["GET"])
# def get_reg():
#     print(request.args)
#     return "注册成功"
#
#
# @app.route('/post/reg', methods=["POST"])
# def post_reg():
#     print(request.form)
#     user = request.form.get("user")
#     hobby = request.form.getlist("hobby")
#     print(user, hobby)
#     return "注册成功"




# https://kunkunruye1.github.io/
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



