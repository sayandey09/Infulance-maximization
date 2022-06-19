from flask import Flask, render_template, redirect, url_for, request
from generate_graph import generate
from compare_algo_main import *
from business_algo_main import *

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/project")
def project():
    return render_template("project.html") 

@app.route("/business", methods = ["GET","POST"])
def business():
    if request.method == "POST":
        clearCache()
        valK = int(request.form.get("seed"))
        valMc = int(request.form.get("mc"))
        file = request.files["data"]
        risS,numberOfActivatedNodes = business_algo(file,valK,valMc)
        return render_template("business_model.html", data = risS, data2 = numberOfActivatedNodes, text = "Seed List = ", text2 = "No. of activated Nodes = ")
    if request.method == "GET":
        clearCache()
        return render_template("business_model.html") 

@app.route("/test", methods = ["GET","POST"])
def test():
    if request.method == "POST":
        clearCache()
        valK = int(request.form.get("seed"))
        valMc = int(request.form.get("mc"))
        valGraph = int(request.form.get("graph"))
        valNode = int(request.form.get("node"))
        nodeList = [i for i in range(100,100+valGraph*valNode,valNode)]
        graphList = generate(valGraph,valNode)
        compare(valK,valMc,graphList,nodeList)
        return render_template("testing_model.html")
    if request.method == "GET":
        clearCache()
        return render_template("testing_model.html") 

if __name__ == "__main__":
    app.run(debug=True)