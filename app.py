from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/quotes")
def quotes():
    return render_template("quotes.html")

@app.route("/review", methods=["GET", "POST"])
def review():
    if request.method == "POST":
        username = request.form.get("username")
        user_review = request.form.get("review")
        return f"Ім’я: {username}. Ваш відгук: {user_review}"
    return render_template("review.html")

app.run(debug=True)








