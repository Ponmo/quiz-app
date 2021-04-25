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
  return render_template('page1.html', disable = Markup(''), disable2 = Markup(''))

#def startOver():
#    session.clear() #clears variable values and creates a new session
#    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page2', methods=['GET','Post'])
def renderPage2():
  session["answer"]=request.form['answer']
  return render_template('page2.html')

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

if __name__=="__main__":
    app.run(debug=True)
