from flask_restful import Resource, reqparse
from model.user_model import UserModel
from flask_jwt_extended import create_access_token


# Classe que tem o método post
# Esse método realiza o login, ele é realizado enviando um objeto
# no body da requisição.
# Se as credenciais estiverem corretas ele retorna o token para ser usado
# nos outros endpoints
class UserLogin(Resource):
    @classmethod
    def post(self):
        attrib = reqparse.RequestParser()
        attrib.add_argument('username', type=str, required=True)
        attrib.add_argument('password', type=str, required=True)

        data = attrib.parse_args()

        user = UserModel.find_user_by_username(data['username'])

        if (user):
            res = user.verify_password(data['password'], user.password)
            if (res):
                access_token = create_access_token(identity=user.user_id)
                return {"token": access_token}, 200
            return {"message": "Username or Password is incorrect"}, 401
