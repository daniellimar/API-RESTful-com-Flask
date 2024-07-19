from flask import Flask, request, jsonify

app = Flask(__name__)

books = []

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    book = request.get_json()
    books.append(book)
    return jsonify(book), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = request.get_json()
    books[book_id] = book
    return jsonify(book)

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    books.pop(book_id)
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)
