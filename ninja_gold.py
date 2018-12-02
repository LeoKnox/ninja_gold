from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'make it so number one'

@app.route('/')
def super_ninja():
    if 'uractivity' not in session:
        session['uractivity']=""
    if 'urgold' not in session:
        session['urgold']=0
    return render_template('ninja_gold.html')

@app.route('/process_money/<activity>')
def process_money(activity):
    if activity=='farm':
        session['urgold']+=random.randint(10,20)
        session['uractivity']+= "You completed " + activity
    elif activity=='cave':
        session['urgold']+=random.randint(5,10)
    elif activity=='house':
        session['urgold']+=random.randint(2, 5)
    elif activity=="casino":
        session['urgold']+=random.randint(-50, 50)
    return redirect('/')

@app.route('/proc/')
def prc():
    session.clear()
    return render_template('ninja_gold.html')

if __name__=="__main__":
    app.run(debug=True)
