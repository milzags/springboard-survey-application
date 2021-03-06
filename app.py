from flask import Flask, render_template, request, redirect, flash, session
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

@app.route('/start', methods=['POST'])
def redirect_to_question():
    """ start the survey, re-direct user to first question """
    """ but check if session storage exists, if not create it """
    if 'responses' not in session:
        session['responses'] = []
        return redirect('/questions/0')
    else:
        return redirect('/questions/0')


@app.route('/questions/<int:num>')
def show_question(num):
    """show the questions one at a time """
    return render_template('questions.html', num=num, survey=current_survey)

@app.route('/answer', methods=['POST','GET'])
def handle_answers():
    global current_question
    if request.method == 'POST':
        answer = request.form['choice']
        choice_list = session['responses']
        choice_list.append(answer)
        session['responses'] = choice_list
        current_question += 1
        return render_template('questions.html', num=current_question, survey=current_survey)
    else:
        pass

@app.route('/complete')
def complete_survey():
    print(session['responses'])
    return render_template('complete.html')