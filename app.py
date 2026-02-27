from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Connect to DB (SQLite)
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    questions = conn.execute('SELECT * FROM questions').fetchall()
    conn.close()
    return render_template('index.html', questions=questions)

@app.route('/question/<int:id>')
def question_page(id):
    conn = get_db_connection()
    question = conn.execute('SELECT * FROM questions WHERE id = ?', (id,)).fetchone()
    answers = conn.execute('SELECT * FROM answers WHERE question_id = ?', (id,)).fetchall()
    conn.close()
    return render_template('question1.html', question=question, answers=answers)

@app.route('/ask', methods=['POST'])
def ask_question():
    title = request.form['title']
    conn = get_db_connection()
    conn.execute('INSERT INTO questions (title) VALUES (?)', (title,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
