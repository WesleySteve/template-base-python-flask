from flask_restful import Api


def load(api: Api) -> Api:
    from app.resources.teste_resource import TesteResource
    api.add_resource(TesteResource, "/testes")


    return api