from createdb import db

# Nessa classe criamos as tabelas do banco
# Criamos os métodos de busca para retornar o registro passando o id.
# Métodos para criar, deletar e atualizar os registros
# O decorator @classmethod quer dizer que o método pode ser acessado pela
# classe não somente pelo objeto


class BookModel(db.Model):
    __tablename__ = 'Book'

    book_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(50), nullable=False)
    book_author = db.Column(db.String(50), nullable=False)
    book_edition = db.Column(db.String(20), nullable=False)

    def __init__(self, book_name, book_author, book_edition):
        self.book_name = book_name
        self.book_author = book_author
        self.book_edition = book_edition

    def json(self):
        return {
            "book_id": self.book_id,
            "book_name": self.book_name,
            "book_author": self.book_author,
            "book_edition": self.book_edition
        }

    def save_book(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as error:
            print(error)

    def delete_book(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as error:
            print(error)

    def update_book(self, book_name, book_author, book_edition):
        self.book_name = book_name
        self.book_author = book_author
        self.book_edition = book_edition

    @classmethod
    def find_book_by_name(cls, book_name):
        book = cls.query.filter_by(book_name=book_name).first()
        if (book):
            return book
        return None

    @classmethod
    def find_book_by_id(cls, book_id):
        book = cls.query.filter_by(book_id=book_id).first()
        if (book):
            return book
        return None
