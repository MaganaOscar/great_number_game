from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = b'\xb3b\xe2\x86\x84\x05\xf2\xc2L\xcd\x11;c\x83u<'
rand = random.randint(1, 100)

@app.route("/")
def index():
    if 'rand' not in session:
        session['rand'] = rand
    if 'reset' in session:
        session['rand'] = session['reset']
    if 'attempts' in session:
        session['attempts'] += 1
    else:
        session['attempts'] = 0
    print(session)
    return render_template("index.html")

@app.route("/guess", methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    if guess == session['rand']:
        session['result'] = 0
        return redirect('/')
    elif guess > session['rand']:
        session['result'] = 1
        return redirect('/')
    else:
        session['result'] = -1
        return redirect('/')

@app.route("/reset", methods=['POST'])
def reset():
    session.clear()
    session['reset'] = random.randint(1, 100)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)