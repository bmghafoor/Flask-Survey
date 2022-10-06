from flask import Flask, render_template, redirect, request, flash
from surveys import satisfaction_survey


app  = Flask(__name__)
SECRET_KEY = 'password123'
app.secret_key = 'password123'

responses = []

@app.route('/')
def homepage():
    return render_template('base.html', title = satisfaction_survey.title, instructions = satisfaction_survey.instructions)

@app.route('/question/<int:num>')
def question(num):

    if len(responses) == len(satisfaction_survey.questions):
        return "Thank You for Completing the Survey, You may exit out this window"

    elif num == len(responses):
        return render_template('index.html', title = satisfaction_survey.title, q = satisfaction_survey.questions[num])

    elif num != len(responses):
        flash('Stop messing with the url')
        return render_template('index.html', title = satisfaction_survey.title, q = satisfaction_survey.questions[len(responses)])
    

@app.route('/answers', methods = ['POST'])
def answer():
    ans = request.form['ans']
    responses.append(ans)
    return redirect(f'/question/{len(responses)}')

