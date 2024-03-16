import mysql.connector

dbconfig = { 'host': 'localhost',
                'user': 'root',
                'password': '2468',
                'database': 'vsearchlogdb', }

#function to check user details(username, password)
def check_user(request,dbconfig=dbconfig):
    #connectin mysql server
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _ALREADY_EXIST = """ select user_name, pswd from accounts
                    where user_name = %s """
    cursor.execute(_ALREADY_EXIST, (request.form['name'],))
    res = cursor.fetchall()
    #closing connection
    conn.commit()
    cursor.close()
    conn.close()
    #returns ([user_name, password],)
    return res

#to check inline users
def onl_users(dbconfig=dbconfig):
    #connectin mysql server
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _ONL_USR = """ select name, port from ousr
                    where actv = 'a' """
    cursor.execute(_ONL_USR)
    res = cursor.fetchall()
    #closing connection
    conn.commit()
    cursor.close()
    conn.close()
    #returns ([user_name, password],)
    return res

def create_usr(request,dbconfig=dbconfig):
    #connectin mysql server
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _CREATE_USR = """ INSERT INTO accounts
                    (user_name,pswd)
                    VALUES
                    (%s, %s)"""
    cursor.execute(_CREATE_USR,(request.form['name'],request.form['password'],))
    #closing connection
    conn.commit()
    cursor.close()
    conn.close()