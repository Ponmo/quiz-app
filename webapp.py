import os
from flask import Flask, request, Markup, url_for, render_template, flash, Markup
from flask import redirect
from flask import session
import time

app = Flask(__name__)

app.secret_key=os.environ["KEY"];
    
@app.route('/')
def renderMain():
  return render_template('home.html')

@app.route('/page1')
def renderPage1():
  settings = ['', '']
  if 'start' not in session:
    session["start"]=time.time()
  if 'answer1' in session:
    settings = checkAnswer('answer1')
  return render_template('page1.html', disable = settings[0], disable2 = settings[1])

@app.route('/page2', methods=['GET','POST'])
def renderPage2():
  settings = ['', '']
  if 'answer2' in session:
    settings = checkAnswer('answer2')
  elif 'answer1' not in session:
    session["answer1"]=request.form['answer']
  return render_template('page2.html', disable3 = settings[0], disable4 = settings[1])

@app.route('/page3', methods=['GET','POST'])
def renderPage3():
  settings = ['', '']
  if 'answer3' in session:
    settings = checkAnswer('answer3')
  elif 'answer2' not in session:
    session["answer2"]=request.form['answer']
  return render_template('page3.html', disable5 = settings[0], disable6 = settings[1])

@app.route('/page4', methods=['GET','POST'])
def renderPage4():
  settings = ['', '']
  if 'answer4' in session:
    settings = checkAnswer('answer4')
  elif 'answer3' not in session:
    session["answer3"]=request.form['answer']
  return render_template('page4.html', disable7 = settings[0], disable8 = settings[1])

@app.route('/page5', methods=['GET', 'POST'])
def renderPage5():
  if 'answer4' not in session:
    session["answer4"]=request.form['answer']
  first = session['answer1']
  second = session['answer2']
  third = session['answer3']
  fourth = session['answer4']
  if 'end' not in session:
    session['end'] = int(time.time() - session['start'])
  number_correct = checkCorrect()
  return render_template('page5.html', answerone = first, answertwo = second, answerthree = third, answerfour = fourth, totaltime = session['end'],score = number_correct)

@app.route('/reset')
def startOver():
  session.clear()
  return redirect(url_for('renderMain'))

def checkAnswer(question_number):
    settings = []
    if session[question_number]=='True':
        settings.append(Markup('checked disabled'))
        settings.append(Markup('disabled'))
    else:
        settings.append(Markup('disabled'))
        settings.append(Markup('checked disabled'))
    return settings

def checkCorrect():
    score = 0
    if session['answer1'] == "True":
        score += 1
    if session['answer2'] == "False":
        score += 1
    if session['answer3'] == "True":
        score += 1
    if session['answer4'] == "False":
        score += 1
    return score
    
if __name__=="__main__":
    app.run(debug=True)
