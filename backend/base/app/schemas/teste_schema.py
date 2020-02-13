from flask_restful import fields


testes_schema = {
    'id': fields.Integer,
    'nome': fields.String,
    'status': fields.Boolean
}