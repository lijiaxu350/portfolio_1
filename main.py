from flask import Flask, render_template, url_for, flash, redirect, request
import git
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", subtitle = "Home Page", text = "This is my landing page")
@app.route("/about")
def about():
    return render_template("about.html", subtitle="About Me")

@app.route("/education")
def education():
    return render_template("education.html", subtitle="Education")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html", subtitle="Contact")

@app.route("/update_server", methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/jiaxuli350/portfolio_1')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400
    
if __name__ == '__main__':
    app.run(debug = True, host = "0.0.0.0")