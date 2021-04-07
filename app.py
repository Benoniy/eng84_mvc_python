from flask import Flask, render_template

# Create an instance of an app
app = Flask(__name__)


# Use a decorator @ to define the homepage
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/welcome/")
def welcome():
    return "Second page"


# Create two more pages and add email and password functionality
@app.route("/register/")
def register():
    return render_template("register.html")


@app.route("/login/")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
