from flask import Flask,render_template,redirect,url_for,request, session, flash

app =  Flask(__name__)

app.secret_key = "sm sm"

@app.route('/')
def home():
    return render_template('home.html')

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
def logout():
    session.pop('logged_in',None)
    flash("hey! you have successfully logged out!")
    return redirect(url_for('home'))

if __name__ ==  '__main__':
    app.run(debug=True)



