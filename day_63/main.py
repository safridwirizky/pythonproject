from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, Float
from pathlib import Path
# import sqlite3



# CREATE DATABASE
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{Path(__file__).resolve().parent / 'books-collection.db'}"
db.init_app(app)

class Books(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    author: Mapped[str]
    rating: Mapped[float]

with app.app_context():
    db.create_all()



# EQUAL TO
'''
db = sqlite3.connect(Path(__file__).resolve().parent / 'books-collection.db')
cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title VARCHAR(250) NOT NULL UNIQUE,
        author VARCHAR(250) NOT NULL,
        rating FLOAT NOT NULL
    )
""")
db.close()
'''



@app.route('/')
def home():
    all_books = db.session.execute(db.select(Books)).scalars().all()
    return render_template('index.html', all_books=all_books)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        rating = request.form['rating']

        new_book = Books(
            title=title,
            author=author,
            rating=rating
        )

        db.session.add(new_book)
        db.session.commit()
        
        return redirect(url_for('home'))

    return render_template('add.html')


@app.route('/edit', methods=['POST', 'GET'])
def edit():
    book_id = request.args.get('id', type=int) or request.form.get('id', type=int)
    if not book_id:
        return "id book is empty", 400
    
    book = db.session.get(Books, book_id)
    if not book:
        return "ID Book not found", 400
    
    if request.method == 'POST':
        book.rating = float(request.form['edit_rating'])
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', book=book)


@app.route("/delete")
def delete():
    book_id = request.args.get('id', type=int)
    book = db.session.get(Books, book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('home'))
    
    return "Book not found", 404


@app.template_filter('smart_int')
def smart_int(value):
    if value.is_integer():
        return int(value)
    return value


if __name__ == "__main__":
    app.run(debug=True)