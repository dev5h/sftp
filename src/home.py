from src import app, render_template
import os

flist = os.listdir(".")
@app.route("/")
def home():
    # return str(flist)
    return render_template("index.html")