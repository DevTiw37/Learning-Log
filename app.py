from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    def __repr__(self):
        return f'<User {self.username}>'
    

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/create-topic')
def create_topic():
    return render_template('create-topic.html')

  

if __name__ == '__main__':
    app.run(debug=True)