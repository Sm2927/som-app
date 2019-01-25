from flask import Flask,render_template,redirect,url_for,request

app =  Flask(__name__)

@app.route('/')
def home():
    return "Hey Sovna!"

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
            return redirect(url_for('home'))
    return render_template('login.html',error=err)

if __name__ ==  '__main__':
    app.run(debug=True)



