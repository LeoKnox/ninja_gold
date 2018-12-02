from flask import Flask, render_template, request, redirect, session
import random
import datetime

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
    now = datetime.datetime.now()
    if activity=='farm':
        x = random.randint(10,20)
        #test=now.strftime('%y-%m-%d %H:%M%p')
        session['urgold']+=x
        #session['uractivity'] += "<p>'You completed ' + {activity} + ' earning $' + {str(x)} + ' ' + {test}</p>"
        session['uractivity']+= "You completed " + activity + " earning $" + str(x) + " " + now.strftime("%y-%m-%d %H:%M%p") + "\r\n"
    elif activity=='cave':
        x=random.randint(5,10)
        session['urgold']+=x
        session['uractivity']+= "You completed " + activity + " earning $" + str(x) + " " + now.strftime("%y-%m-%d %H:%M%p") + "\r\n"
    elif activity=='house':
        x=random.randint(2, 5)
        session['urgold']+=x
        session['uractivity']+= "You completed " + activity + " earning $" + str(x) + " " + now.strftime("%y-%m-%d %H:%M%p") + "\r\n"
    elif activity=="casino":
        x=random.randint(-50, 50)
        session['urgold']+=x
        session['uractivity']+= "You completed " + activity + " earning $" + str(x) + " " + now.strftime("%y-%m-%d %H:%M%p") + "\r\n"
    return redirect('/')

@app.route('/x/')
def x():
    session.clear()
    return redirect('ninja_gold.html')

if __name__=="__main__":
    app.run(debug=True)
