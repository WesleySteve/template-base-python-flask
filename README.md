# template-base-python-flask

# passos para iniciar um novo projeto baseado neste

- clone o repositório git clone https://github.com/WesleySteve/template-base-python-flask.git
- altere o no da pasta template-base-python-flask (para outro nome)
- dentro do diretório backend possui um diretório com nome de base
- altere este nome (base) para o nome do seu projeto. ex: loja
- acesse o diretório com o nome do seu projeto e instale as dependencias, 
comandos (pipenv install) e (pipenv install --dev)

# para verificar se está tudo ok!

- rode os comandos a seguir
- (pipenv shell) - para acessar o ambiente virtual
- (flask db init) - para inicializar um banco de dados de desenvolvimento com sqlite3
- (flask db migrate) - para preparar o banco de dados
- (flask db upgrade) - para gravar as alterações no banco de dados

# rodando o projeto

- (flask run) - par iniciar o projeto
- acesse um aplicativo de visualização de rest. ex: insomnia
- a url base para teste é:  http://localhost:3001/api/v1/testes - rota (GET, POST),
- json {"nome": "teste"} - para rota (POST)

# para rodar os testes

- rode o comando abaixo estando dentro do diretório (base) ou do nome que você definiu no inicio do projeto
- pytest tests/integration/
- coverage run --source=app -m pytest -s tests/ -v (gerar os arquivos de cobertura do codigo)
- coverage report (visualizar no terminal a % de cobertura do codigo)
- coverage html (gerar o html de forma grafica da % de cobertura do codigo)

# adicione no arquivo .gitignore dentro do diretório backend

- no final do arquivo altere esses dois caminhos:
  (base/.vscode base/migrations) -> para o nome do seu projeto 
  ex: loja/.vscode loja/migrations
- 