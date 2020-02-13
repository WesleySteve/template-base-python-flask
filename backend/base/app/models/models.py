from app import db



class Teste(db.Model):
  __tablename__ = 'teste'
  id = db.Column(db.Integer, autoincrement=True, primary_key=True)
  nome = db.Column(db.String(100), nullable=False, unique=False, index=True)
  status = db.Column(db.Boolean, default=True)
    
    
  def __repr__(self):
    return f"<%Teste: {self.nome} %>"