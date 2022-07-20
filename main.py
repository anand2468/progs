from flask import Flask, render_template, request, redirect, session
import mysql.connector

from comands import check_user, onl_users, create_usr

app=Flask(__name__)
app.secret_key = 'YouWillNeverGuess'

@app.route('/login', methods=['post','get'])
def login():
    #if method = post
    if request.form :
        msg = ''
        #checking user
        res = check_user(request)
        #if the account dosent match
        if len(res)==0:
            msg = 'no account found'
            return render_template('login.html', msg=msg)
        #if account match
        else:
            #if the password macth 
            if res[0][1]==request.form['password']:
                usr = res[0][0]
                session['logedin']= True
                session['user']=str(res[0][0])
                return redirect('/')
            #if entered wrong password
            else:
                msg = 'incorrect password!'
                value = request.form['name']
                return render_template('login.html', msg=msg, value = value)
    #if the method is get
    else:
        return render_template('login.html')

@app.route('/signup', methods=['post', 'get'])
def signup():
    if request.form :
        msg = ''
        name = request.form['name']
        #checking user
        res = check_user(request)
        #creating account
        if len(res)==0:
            create_usr(request)
            session['logedin']= True
            session['user']=request.form['name']
            return redirect('/')
        elif res[0][0]==name:
            msg = 'account already exist!'
            value = request.form['name']
            return render_template('signup.html', msg=msg, value = value)
        
    else:
        return render_template('signup.html')

@app.route('/')
def homepg():
    if session:
        return render_template('hmpg.html', 
        name_of_user = session['user'],
        users = onl_users())
    else:
        return 'hello <a href="/login">sign in</a>'

@app.route('/logout', methods=['post'])
def logout():
    session.pop('logedin')
    session.pop('user')
    return f'you are loged out sucessfully '


if __name__=='__main__':
    app.run(debug=True)
    app.config['SERVER_NAME']='helo:80'