from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configuring the connection to the RDS database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('mydbinstance.ct6ioac42ue3.us-west-2.rds.amazonaws.com')  # This should be set to your RDS endpoint
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Deal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

@app.route('/')
def index():
    return render_template('index.html', clients=Client.query.all(), tasks=Task.query.all(), deals=Deal.query.all(), events=Event.query.all())

@app.route('/add_client', methods=['POST'])
def add_client():
    client_name = request.form['client_name']
    new_client = Client(name=client_name)
    db.session.add(new_client)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_client/<int:id>', methods=['GET'])
def delete_client(id):
    client = Client.query.get_or_404(id)
    db.session.delete(client)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_task', methods=['POST'])
def add_task():
    task_name = request.form['task_name']
    new_task = Task(name=task_name)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_event', methods=['POST'])
def add_event():
    event_name = request.form['event_name']
    new_event = Event(name=event_name)
    db.session.add(new_event)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_deal', methods=['POST'])
def add_deal():
    deal_name = request.form['deal_name']
    new_deal = Deal(name=deal_name)
    db.session.add(new_deal)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
