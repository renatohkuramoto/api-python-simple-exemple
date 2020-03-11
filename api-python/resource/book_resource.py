from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from model.book_model import BookModel


# Essa classe é responsável por gerir as requisições
# GET/POST/PUT/DELET
# O decorator @jwt_requerid é colocado antes da função para dizer
# que para acessar esse método é necessário enviar o token na requisição.
# O método put realiza a função do post, pois se vc tentar atualizar um registro
# e ele não estiver na base, ele irá registrá-lo
class BookResource(Resource):
    @jwt_required
    def get(self, book_id):
        book = BookModel.find_book_by_id(book_id)
        if (book):
            return book.json(), 200
        return {"message": "Book not found"}, 404

    @jwt_required
    def delete(self, book_id):
        book = BookModel.find_book_by_id(book_id)
        if (book):
            book.delete_book()
            return {"message": "Book deleted"}, 200
        return {"message": "Book not found"}, 404

    @jwt_required
    def put(self, book_id):
        attrib = reqparse.RequestParser()
        attrib.add_argument('book_name', type=str, required=True)
        attrib.add_argument('book_author', type=str, required=True)
        attrib.add_argument('book_edition', type=str, required=True)

        data = attrib.parse_args()

        book_found = BookModel.find_book_by_id(book_id)

        if (book_found):
            book_found.update_book(**data)
            book_found.save_book()
            return {"message": "Book updated"}, 200
        book = BookModel(**data)
        book.save_book()
        return {"message": "Book created"}, 201
