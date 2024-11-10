from flask import Flask, render_template, request, redirect, session, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key' 

@app.route('/', methods=['GET', 'POST'])
def gng():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
    
    if request.method == 'POST':
        guess = int(request.form['guess'])
        
        if guess == session['number']:
            return render_template('gng.html', message="You guessed it! 🎉", play_again=True)
        elif guess > session['number']:
            return render_template('gng.html', message="Too high! ⬆️" , play_again=False)
        else:
            return render_template('gng.html', message="Too low! ⬇️" , play_again=False)
    
    return render_template('gng.html', message="")

@app.route('/play_again')
def play_again():
    session.pop('number', None)
    return redirect(url_for('gng'))

if __name__ == '__main__':
    app.run(debug=True)
