from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flusk_crud'

mySql = MySQL(app)

all_post = [
    {
        'title': 'hello world',
        'author': 'abc'
    },
    {
        'title': 'hello world 2',
    }
]

@app.route('/home/<string:name>')
def hello(name):
    return render_template('index.html')

@app.route('/post')
def post():
    return render_template('post.html', posts=all_post)

@app.route('/add-post')
def addPostView():
    return render_template('add-post.html')

@app.route('/api/add-post', methods=['POST'])
def addPost():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        author = request.form['author']

        cur = mySql.connection.cursor()
        cur.execute("INSERT INTO posts (title, description, author) VALUES (%s, %s, %s)", (title, description, author))
        mySql.connection.commit()
        return redirect(url_for('post'))


if __name__ == "__main__":
    app.run(debug=True)