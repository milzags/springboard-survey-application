from flask import Flask, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import Survey, Question, surveys

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)
current_survey = surveys['satisfaction']
current_question = 0

responses = []
#as people answer questions, store the responses in this empty list.


@app.route('/')
def show_survey_information():
    """ show the user the title of the survey, the instructions and a button to start the survey """
    return render_template('survey.html',survey=current_survey)

@app.route('/questions')
def redirect_question():
    """ start the survey, re-direct user to first question """
    return redirect('/questions/0')

@app.route('/questions/<int:num>')
def show_question(num):
    """show the questions one at a time """
    return render_template('questions.html', num=num)

@app.route('/answer/<num>')
def append_answer():
    responses.append(answer)
    flash('Answer added to database')
    return redirect('/questions/<int:num>')