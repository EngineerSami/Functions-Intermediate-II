from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def gng():
    if 'visit_count' in session:
        session['visit_count'] += 1
    else:
        session['visit_count'] = 1
    return render_template('counter.html', visit_count=session['visit_count'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
