from flask import Flask, jsonify, redirect, render_template, request, url_for
from calculator import Calculate

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit",methods = ["POST","GET"])
def submit():
    if request.method == "POST":
        time1 = request.form["date1"]
        time2 = request.form["date2"]

        date1 = time1.split("-")
        date2 = time2.split("-")

        difference = Calculate(date1,date2)

        return jsonify(f"<b>{difference.years}</b> Years<br><b>{difference.months}</b> Months<br><b>{difference.days}</b> Days")

    else:
        print("hi")
        return redirect(url_for("home"))

@app.errorhandler(404)
def error(e):
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
