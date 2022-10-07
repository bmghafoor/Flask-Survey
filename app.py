from flask import Flask, render_template, redirect, request, flash, session
from surveys import satisfaction_survey


app  = Flask(__name__)
SECRET_KEY = 'password123'
app.secret_key = 'password123'

responses = []

@app.route('/start', methods = ['POST'])
def start():
    session['responses'] = []
    return redirect('/question/0')

@app.route('/')
def homepage():
    return render_template('base.html', title = satisfaction_survey.title, instructions = satisfaction_survey.instructions)

@app.route('/question/<int:num>')
def question(num):

    if len(session['responses']) == len(satisfaction_survey.questions):
        return "Thank You for Completing the Survey, You may exit out this window"

    elif num == len(session['responses']):
        return render_template('index.html', title = satisfaction_survey.title, q = satisfaction_survey.questions[num])

    elif num != len(session['responses']):
        flash('Stop messing with the url')
        return render_template('index.html', title = satisfaction_survey.title, q = satisfaction_survey.questions[len(session['responses'])])
    

@app.route('/answers', methods = ['POST'])
def answer():
    ans = request.form['ans']
    responses = session['responses']
    responses.append(ans)
    session['responses'] = responses
    id = len(session['responses'])
    return redirect(f'/question/{id}')


