import pytest
import json
from app import create_app, db
from app.models.models import Teste




@pytest.fixture
def web():
  app = create_app('testing')
  context = app.app_context()
  context.push()

  db.create_all()

  yield app.test_client()

  db.drop_all()
  db.session.remove()

  context.pop



def test_obter_todos_testes_api(web, snapshot):

  teste = Teste()
  teste.nome = "Intel"

  teste1 = Teste()
  teste1.nome = "AMD"

  teste2 = Teste()
  teste2.nome = "HP"

  db.session.add(teste)
  db.session.add(teste1)
  db.session.add(teste2)

  db.session.commit()

  response = web.get("/api/v1/testes")

  snapshot.assert_match(response.json)
  
  

def test_adicionar_teste(web, snapshot):
  headers = {"Accept": "application/json", "Content-Type": "application/json"}  
  
  payload = {"nome": "teste adicionar"}
  
  response = web.post("/api/v1/testes", data=json.dumps(payload), headers=headers)
  
  snapshot.assert_match(response.json)
  