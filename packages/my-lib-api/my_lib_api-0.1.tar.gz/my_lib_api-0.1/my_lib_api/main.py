from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

#app
app = Flask(__name__, template_folder='templates')

#config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
app.config['UPLOAD_FOLDER'] = 'library_api/uploads'

#database obj
db = SQLAlchemy(app)

class Books(db.Model):
    book_id = db.Column(db.Integer, primary_key = True)
    book_name = db.Column(db.String(100), nullable = False)
    author = db.Column(db.String(50), nullable = False)
    price = db.Column(db.Float, nullable = False)
    
    def convert_to_dict(self):
        return {
            "book_id" : self.book_id,
            "book_name" : self.book_name,
            "author" : self.author,
            "price" : self.price
        }

#routes
@app.route('/')
def home():
    return jsonify({"message":'Welcome to Library'})

#fetch all the books in db
@app.route('/library',methods = ['GET'])
def get_library():
    library = Books.query.all()

    return jsonify([book.convert_to_dict() for book in library])

#fetch particular book from db
@app.route('/library/<int:book_id>', methods = ['GET'])
def get_book(book_id):
    book = Books.query.get(book_id)

    if book:
        return jsonify(book.convert_to_dict())
    else:
        return jsonify({"error" : "Book not found"}), 404
    pass

#write data to db
#POST
@app.route('/library', methods = ['POST'])
def add_book():
    data = request.get_json()

    new_book = Books(
        book_name = data['book_name'],
        author = data['author'],
        price = data['price']
    )

    db.session.add(new_book)
    db.session.commit()

    return jsonify(new_book.convert_to_dict()), 201

#PUT /Update
@app.route("/library/<int:book_id>", methods = ['PUT'])
def update_book(book_id):
    data = request.get_json()

    book = Books.query.get(book_id)

    if book:
        book.book_name = data.get("book_name", book.book_name)
        book.author = data.get("author", book.author)
        book.price = data.get("price", book.price)

        db.session.commit()

        return jsonify(book.convert_to_dict())
    else:
        return jsonify({'error': "Book Not Found"}), 404

#Delete
@app.route('/library/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Books.query.get_or_404(book_id)

    if book:
        db.session.delete(book)
        db.session.commit()

        return jsonify({'message':'Book Deleted'})
    else:
        return jsonify({'error':'Book Not Found.'}),404

#upload file
@app.route('/upload', methods = ['GET','POST'])
def file_upload():
    if request.method == 'POST':
        os.makedirs('library_api/uploads', exist_ok=True) #makes uploads folder if it doesnt exist 

        file = request.files['post_file']
        try:
            if file:
                file_name = secure_filename(file.filename)
                save_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
                file.save(save_path)
                return 'File Uploaded Successfully'
        except Exception as e:
            return f'{e}', 404

    return render_template('import_file.html')

def create_database():
    with app.app_context():
        db.create_all()
    
def launch_app():
    create_database()
    app.run()

#run
if __name__ == '__main__':
    create_database()

    app.run(debug=True)