# Importando as bibliotecas
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

# Importando os scripts
from resource.user_resource import UserLogin
from resource.book_resource import BookResource
from model.user_model import UserModel
from createdb import db

# Instanciândo a aplicação
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Tipo do banco de dados
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_SECRET_KEY'] = 'FRASESECRETA'  # SECRET do Token JWT
api = Api(app)
jwt = JWTManager(app)
db.init_app(app)

# Decorator que executa antes da primeira requisição
# Se não tiver a base de dados ele irá criar e adicionar um usuário
@app.before_first_request
def createdb():
    db.create_all()
    admin = {"username": "admin", "password": "1234"}
    user = UserModel(**admin)
    user.save_user()


# Endpoints ou rotas da aplicação
api.add_resource(UserLogin, '/login')
api.add_resource(BookResource, '/book/<string:book_id>')


# Executa
if __name__ == '__main__':
    app.run()
