import os
from flask import Flask, request, Markup, url_for, render_template, flash, Markup
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["KEY"];
    
@app.route('/')
def renderMain():
  return render_template('home.html')

@app.route('/page1')
def renderPage1():
  settings = ['', '']
  if 'answer1' in session:
    settings = checkAnswer('answer1')
  return render_template('page1.html', disable = settings[0], disable2 = settings[1])

@app.route('/page2', methods=['GET','POST'])
def renderPage2():
  if 'answer1' not in session:
    session["answer1"]=request.form['answer']
  return render_template('page2.html', disable3 = Markup(''), disable4 = Markup(''))

@app.route('/page3', methods=['GET','POST'])
def renderPage3():
  session["answer2"]=request.form['answer']
  return render_template('page3.html')

@app.route('/page4', methods=['GET','POST'])
def renderPage4():
  session["answer3"]=request.form['answer']
  return render_template('page4.html')

@app.route('/page5', methods=['GET', 'POST'])
def renderPage5():
  session["answer4"]=request.form['answer']
  return render_template('page5.html')

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
    
if __name__=="__main__":
    app.run(debug=True)
