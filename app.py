from flask import Flask,request, redirect, render_template
app=Flask(__name__)
@app.route('/me', methods=['GET'])
def me():
    return render_template('pierwsza_strona.html')
@app.route('/contact',methods=['POST','GET'])
def contact():
    if request.method=="GET":
        return render_template("druga_strona.html")
    elif request.method=="POST":
        print(request.form)
        return redirect("/contact")