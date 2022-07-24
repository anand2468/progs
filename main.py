from flask import Flask, render_template, request, redirect, session
from comands import check_user, onl_users, create_usr

app=Flask(__name__)
app.secret_key = 'YouWillNeverGuess'

@app.route('/login', methods=['post','get'])
def login():
    #if method = post
    if request.method == 'POST' :
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
                #session['id']=str(res[0][2])#change
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
    if request.method == 'POST' :
        name = request.form['name']
        #checking user
        res = check_user(request)
        print(res)
        print(len(res))
        if len(res)!=0:
            if res[0][0]==name:
                msg = 'account already exist!'
                value = request.form['name']
                return render_template('signup.html', msg=msg, value = value)
        if len(request.form['password'])<8 and len(request.form['name'])<8 :
            msg = 'check username and password!'
            value = request.form['name']
            return render_template('signup.html', msg=msg, value = value)
        #creating account
        elif len(res)==0 and len(request.form['password'])>=8 and len(request.form['name'])>=8:
            create_usr(request)
            session['logedin']= True
            session['user']=request.form['name']
            return redirect('/')
    else:
        return render_template('signup.html')

@app.route('/')
def homepg():
    if session:
        return render_template('hmpg.html', 
        name_of_user = session['user'],
        users = onl_users())
        #users = chatt()#change
    else:
        return render_template('signup.html')

@app.route('/logout', methods=['post',"get"])
def logout():
    session.pop('logedin')
    session.pop('user')
    return f'you are loged out sucessfully <a href="/"> log in </a>clear'

@app.route('/dummy/<user>')
def ntg(user=12):
    return render_template("demopg.html",namee = user)

if __name__=='__main__':
    app.run(debug=True,port="80",host="0.0.0.0")
