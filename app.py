from flask import Flask,request,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from operations import *


app = Flask(__name__)
# Database Configuration , see SQLAlchemy documentation
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Funct(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    desc = db.Column(db.String(300),nullable=True)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)


@app.route('/',methods=['POST','GET'])
def perform():
    x = {}
    if request.method=='POST':
            a = int(request.form['first'])
            b = int(request.form['second'])
            operation = request.form['operation']
            print(a,b,operation)
            if operation == "addition":
                x = addition(a,b)
            elif operation == "subtract":
                x = sub(a,b)
            elif operation == "multiply":
                x = multiply(a,b)
            elif operation == "divide":
                x = divide(a,b)
            elif operation == "add":
                return redirect(url_for('add'))
    
    return render_template('index.html',x=x)

@app.route('/add',methods=['POST','GET'])
def add():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        #creating an object of class Funct with column names to be added
        todo = Funct(title=title, desc=desc)
        #commitiing columns into db
        db.session.add(todo)
        db.session.commit()

    # Quering the db for info
    alltodo = Funct.query.all()

    # Passing qeuried info to index.html
    return render_template('add.html', alltodo = alltodo)

@app.route('/update/<int:sno>', methods=['GET','POST'])
def update_data(sno):
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']

        # Quering all info with filter by sno and first occurence
        todo = Funct.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/add")
    
    # Quering the info by sno and first occurence
    todo = Funct.query.filter_by(sno=sno).first()
    # Sending the info to update.html with todo
    return render_template('update.html', todo = todo)


@app.route('/delete/<int:sno>')
def delete_data(sno):
    todo = Funct.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/add")

if __name__ == "__main__":
    app.run(debug=True)