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
  settings = ['', '']
  if 'answer1' not in session:
    session["answer1"]=request.form['answer']
  if 'answer2' in session:
    settings = checkAnswer('answer2')
  return render_template('page2.html', disable3 = settings[0], disable4 = settings[1])

@app.route('/page3', methods=['GET','POST'])
def renderPage3():
  settings = ['', '']
  if 'answer2' not in session:
    session["answer2"]=request.form['answer']
  if 'answer3' in session:
    settings = checkAnswer('answer3')
  return render_template('page3.html', disable5 = settings[0], disable6 = settings[1])

@app.route('/page4', methods=['GET','POST'])
def renderPage4():
  settings = ['', '']
  if 'answer3' not in session:
    session["answer3"]=request.form['answer']
  if 'answer4' in session:
    settings = checkAnswer('answer4')
  return render_template('page4.html', disable7 = settings[0], disable8 = settings[1])

@app.route('/page5', methods=['GET', 'POST'])
def renderPage5():
  if 'answer4' not in session:
    session["answer4"]=request.form['answer']
  result = Markup('<h2>Polymers are formed by dehydation synthesis reactions.</h2><br>' + '<p>Your answer: </p>' + session["answer1"] + '<br>' + '<p>Correct answer: True</p><br>' +
                 '<h2>Enzymes are used to make substrates.</h2><br>' + '<p>Your answer: </p>' + session["answer2"] + '<br>' + '<p>Correct answer: False</p><br>' +
                 '<h2>Carbon fixation means transforming carbon into a more useful form.</h2><br>' + '<p>Your answer: </p>' + session["answer3"] + '<br>' + '<p>Correct answer: True</p><br>' +
                 '<h2>If an area has high water potential, it means the water there will move to an area with less solute density.</h2><br>' + '<p>Your answer: </p>' + session["answer4"] + '<br>' + '<p>Correct answer: False</p><br>')
  return render_template('page5.html', results = result)

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
