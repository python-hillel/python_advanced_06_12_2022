import sqlite3
from flask import request

from flask import Flask, render_template, redirect

import csv

app = Flask(__name__)


@app.route('/')
def index():
    # return "* Serving Flask app 'application'<br>" \
    #        "* Debug mode: on"
    return render_template('index.html', title='Index page', content='Hello World!')


@app.route('/book/list')
def read_books():
    c = sqlite3.connect('book.db')
    cr = c.cursor()
    cr.execute('SELECT * FROM book;')
    res = cr.fetchall()
    cr.close()
    c.close()

    return render_template('list.html', title='List of books', books=res)


@app.route('/book/detail/<int:pk>')     # /book/detail/4
def detail(pk):
    c = sqlite3.connect('book.db')
    cr = c.cursor()
    cr.execute('SELECT * FROM book WHERE id = ?', (pk,))
    res = cr.fetchone()
    cr.close()
    c.close()

    if res is None:
        return render_template('index.html', title='Page not found', content='404 - Page not found')

    return render_template('detail.html', title='Book detail', book=res)


@app.route('/book/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        if title and author:
            c = sqlite3.connect('book.db')
            cr = c.cursor()
            cr.execute('INSERT INTO book(title, author) VALUES (?, ?);', (title, author))
            c.commit()
            cr.close()
            c.close()
            return redirect('/book/list')

    return render_template('create.html', title='Create new book')


@app.route('/book/update/<int:pk>', methods=['GET', 'POST'])
def update(pk):
    c = sqlite3.connect('book.db')
    cr = c.cursor()
    cr.execute('SELECT * FROM book WHERE id = ?', (pk,))
    res = cr.fetchone()

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        if title and author:
            cr.execute('UPDATE book SET title = ?, author = ? WHERE id = ?;', (title, author, pk))
            c.commit()
            cr.close()
            c.close()
            return redirect('/book/list')

    return render_template('update.html', title='Update book', book=res)


@app.route('/book/delete/<int:pk>', methods=['GET', 'POST'])
def delete(pk):
    c = sqlite3.connect('book.db')
    cr = c.cursor()
    cr.execute('SELECT * FROM book WHERE id = ?', (pk,))
    res = cr.fetchone()

    if request.method == 'POST':
        cr.execute('DELETE FROM book WHERE id = ?', (pk, ))
        c.commit()
        cr.close()
        c.close()
        return redirect('/book/list')

    return render_template('delete.html', title='Delete book', book=res)


app.run(debug=True, port=12345)
