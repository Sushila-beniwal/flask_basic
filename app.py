from flask import Flask,render_template,url_for,redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/passed/<name>/<int:marks>")
def passed(name,marks):
    return render_template("passe.html",title="result")


@app.route("/passed/<name>/<int:marks>")
def fail(name,marks):
    return render_template("fail.html",title="result")

@app.route("/result/<sname>/<int:mark>")
def result(sname,mark):
    if mark<30:
        return redirect("fail",name=sname,marks=mark)
    else:
        return redirect("passed",name=sname,marks=mark)

if __name__=="__main__":
    app.run(host="0.0.0.0")
