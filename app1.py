from flask import Flask,render_template,redirect,\
    url_for,request, session, flash,g
from functools import  wraps
import sqlite3

app =  Flask(__name__)

app.secret_key = "sm sm"
app.database = "sample.db"

def reqlog(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@reqlog
def home():
    g.db = connect_db()
    cur  = g.db.execute('select * from posts')
    posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    g.db.close()
    return render_template('home.html', posts=posts)

@app.route('/comein')
def comein():
    return render_template('comein.html')

@app.route('/login', methods=['GET','POST'])
def login():
    err = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'password':
            err = 'Invalid username or password. Please try again.'
        else:
            session['logged_in'] = True
            flash("hey! you have successfully logged in!")
            return redirect(url_for('comein'))
    return render_template('login.html',error=err)

@app.route('/logout')
@reqlog
def logout():
    session.pop('logged_in',None)
    flash("hey! you have successfully logged out!")
    return redirect(url_for('home'))

def connect_db():
    return sqlite3.connect(app.database)

if __name__ ==  '__main__':
    app.run(debug=True)



