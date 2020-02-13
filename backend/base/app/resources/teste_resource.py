from flask_restful import Resource, marshal, reqparse

from app.models.models import Teste as TesteModel
from app.schemas.teste_schema import testes_schema
from app import db


class TesteResource(Resource):
  def get(self):
    testes = TesteModel.query.all()
    return marshal(testes, testes_schema, 'testes')
  
  
  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument('nome', required=True, help='O campo nome é obrigatório')


    payload = parser.parse_args()

    testes = TesteModel()
    testes.nome = payload.nome


    db.session.add(testes)
    db.session.commit()

    return marshal(testes, testes_schema, 'teste')