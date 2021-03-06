from flask import Flask

app = Flask(__name__)

from flask import request, redirect

from flask import render_template

@app.route('/message', methods=['GET', 'POST'])
def message():
   if request.method == 'GET':
       print("We received GET")
       return render_template("form.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")

@app.route('/greeting', methods=['GET', 'POST'])
def greeting():
   if request.method == 'GET':
       print("We received GET")
       return render_template("greeting.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")

@app.route('/busscard', methods=['GET', 'POST'])
def busscard():
   if request.method == 'GET':
       print("We received GET")
       return render_template("busscard.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")

@app.route('/aboutme', methods=['GET', 'POST'])
def aboutme():
   if request.method == 'GET':
       print("We received GET")
       return render_template("aboutme.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
   if request.method == 'GET':
       print("We received GET")
       #print(f"{whatever}")
       #text = request.form['whatever']
       #return render_template('test.html', value1=text)
       return render_template("contact.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/busscard")

