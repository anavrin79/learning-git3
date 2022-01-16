from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def root():
   if request.method == 'GET':
       print("We received GET")
       return render_template("omnie.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")

@app.route('/omnie', methods=['GET', 'POST'])
def omnie():
   items = ["raz", "dwa", "trzy"]
   if request.method == 'GET':
       print("We received GET")
       return render_template("omnie.html", items=items)
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")

@app.route('/kontakt', methods=['GET', 'POST'])
def contact():
   if request.method == 'GET':
       print("We received GET")
       return render_template("kontakt.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")