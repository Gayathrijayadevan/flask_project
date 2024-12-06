from flask import Flask,render_template,redirect,request,url_for
app=Flask(__name__)
import sqlite3

con = sqlite3.connect('data.db') 
try:
    con.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
except:
    pass    

@app.route('/')
def fun1():
    return "welcome"

@app.route('/fun2')
def fun2():
    return"sample fun"

@app.route('/demo_index',methods=['POST','GET'])
def fun3():
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']

        con = sqlite3.connect('data.db')
        con.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
        con.commit()
        con.close()
        print(name,age)

        
        return redirect(url_for('fun3'))
    else:
        con=sqlite3.connect('data.db')
        cursor=con.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        return render_template('demo_index.html', users=users)

@app.route('/index')
def fun4():
    return render_template('index.html')



app.run()



