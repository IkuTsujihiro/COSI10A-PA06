"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import hangman_app
app = Flask(__name__)

global state
state = {'guesses':[],
         'word':"interesting",
		 'word_so_far':"-----------",
		 'done':False,
		 'guesses_left':6,
		 'result':"none"}

@app.route('/')
@app.route('/main')
def main():
	return render_template('hangman.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/start')
def play():
	global state
	state['done'] = False
	state['word'] = hangman_app.generate_random_word()
	state['guesses'] = []
	state['guesses_left'] = 6
	state['word_so_far'] = hangman_app.print_word(state['word'], state['guesses'])
	return render_template("start.html",state=state)

@app.route('/play',methods=['GET','POST'])
def hangman():
	""" plays hangman game """
	global state
	if request.method == 'GET':
		return play()

	elif request.method == 'POST':
		letter = request.form['guess']
		# check if letter has already been guessed
		if letter and letter in state['guesses']:
			state['guesses_left'] -= 1
			state['result'] = "duplicate"
			return render_template("play.html", state=state)
		# check if letter is in word
		elif letter and letter in state['word']:
			state['guesses'] += [letter]
			state['word_so_far'] = hangman_app.print_word(state['word'], state['guesses'])
			state['result'] = "correct"
			# check if the whole word has been guessed
			if len(state['word']) == hangman_app.correct_guesses(state['word'], state['guesses']):
				state['done'] = True
			return render_template("play.html", state=state)
		# otherwise, wrong guess
		else:
			state['guesses'] += [letter]
			state['guesses_left'] -= 1
			state['result'] = "wrong"
		return render_template('play.html',state=state)
		


if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
