from application import app
from application import db

from flask import request
from flask import render_template
from flask import redirect
from flask import url_for

from application.models import Book
from application.forms import CreateBookForm
from application.forms import DeleteBookForm
from application.forms import UpdateBookForm


@app.route('/')
def index():
    return render_template('index.html', title='Index page', content='Hello World!')


@app.route('/book/list')
def read_books():
    books = Book.query.all()

    return render_template('list.html', title='List of books', books=books)


@app.route('/book/detail/<int:pk>')     # /book/detail/4
def detail(pk):
    book = Book.query.filter_by(id=pk).first()

    if book is None:
        return render_template('index.html', title='Page not found', content='404 - Page not found')

    return render_template('detail.html', title='Book detail', book=book)


@app.route('/book/create', methods=['GET', 'POST'])
def create():
    form = CreateBookForm()

    if form.validate_on_submit():
        book = Book(title=form.title.data, author=form.author.data)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('read_books'))

    return render_template('create.html', title='Create new book', form=form)


@app.route('/book/update/<int:pk>', methods=['GET', 'POST'])
def update(pk):
    book = Book.query.get(pk)
    form = UpdateBookForm()

    if form.validate_on_submit():
        book.title = form.title.data
        book.author = form.author.data
        db.session.commit()
        return redirect(url_for('read_books'))
    elif request.method == 'GET':
        form.title.data = book.title
        form.author.data = book.author

    return render_template('update.html', title='Update book', book=book, form=form)


@app.route('/book/delete/<int:pk>', methods=['GET', 'POST'])
def delete(pk):
    book = Book.query.get(pk)
    form = DeleteBookForm()

    if form.validate_on_submit():
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('read_books'))

    return render_template('delete.html', title='Delete book', book=book, form=form)
