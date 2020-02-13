import pytest
import app
from flask import Flask


class TestFLaskApp():
  def test_create_app_deve_existir(self):
    assert(
      hasattr(app, 'create_app'),
      True,
      'app factory não existe'
    )
    
  def test_create_app_deve_ser_invocavel(self):
    assert(
      hasattr(app.create_app, '__call__'),
      True,
      'create_app não é invocavel'
    )
    
  def test_create_app_deve_retornar_um_flask_app(self):
        
    isinstance(
       app.create_app,
       Flask
    )
    
    