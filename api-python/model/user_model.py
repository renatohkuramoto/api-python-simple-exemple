from createdb import db
from passlib.hash import sha256_crypt  # Faz a criptografia da senha
# A senha é criptografada antes de ser salva no banco de dados.

# Nessa classe criamos as tabelas do banco
# Criamos os métodos de busca para retornar o registro passando o id.
# Métodos para criar, deletar e atualizar os registros
# O decorator @classmethod quer dizer que o método pode ser acessado pela
# classe não somente pelo objeto


class UserModel(db.Model):
    __tablename__ = 'Usuario'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    @classmethod
    def find_user_by_username(cls, username):
        user = cls.query.filter_by(username=username).first()
        if user:
            return user
        return None

    def save_user(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception:
            db.session.rollback()
            db.session.close()

    def set_password(self, password):
        self.password = sha256_crypt.encrypt(password)

    def verify_password(self, pass_send, pass_database):
        try:
            return (sha256_crypt.verify(pass_send, pass_database))
        except ValueError:
            return (False)
