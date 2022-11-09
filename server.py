from flask import Flask, render_template,request,redirect,session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route("/")
def home():
    if 'count' not in session:
        session['count']= 0
        return render_template('index.html', count=session['count'])

    if 'count' in session:
        session['count']=  session['count'] + 1
    return render_template('index.html', count=session['count'])


@app.route('/reset')
def button():
    session.clear()
    return  redirect('/')
    
if __name__ == "__main__":
    app.run(debug=True)

