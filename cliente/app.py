import grpc
import proto.game_pb2_grpc as game_pb2_grpc
import  proto.game_pb2 as game_pb2
from user.User import User


class Requests():
    def __init__(self):
        self.empty = game_pb2.google_dot_protobuf_dot_empty__pb2.Empty()

    def sayHello(self):
        with grpc.insecure_channel('127.0.0.1:50051', options=(('grpc.enable_http_proxy', 0), ('grpc.default_authority', 'localhost'))) as channel:
            self.stub = game_pb2_grpc.GameServiceStub(channel)
            response = self.stub.sayHello(self.empty)
            print(f"Resposta do servidor: {response.string}")

    def cadastrarCliente(self, name):
        with grpc.insecure_channel('127.0.0.1:50051', options=(('grpc.enable_http_proxy', 0), ('grpc.default_authority', 'localhost'))) as channel:
            self.stub = game_pb2_grpc.GameServiceStub(channel)
            stringRequest = game_pb2.StringRequest(string=name)
            response = self.stub.cadastrarCliente(stringRequest)
            user = User(name=response.name, chave=response.chave)
            print(f"Usuário {response.name} cadastrado com sucesso!!!")
            return user

    def acessarSala(self, name, user):
        with grpc.insecure_channel('127.0.0.1:50051', options=(('grpc.enable_http_proxy', 0), ('grpc.default_authority', 'localhost'))) as channel:
            self.stub = game_pb2_grpc.GameServiceStub(channel)
            salaRequest = game_pb2.SalaRequest(name = name,token = user.chave)
            response = self.stub.acessarSala(salaRequest)
            print(f"Resposta do servidor: {response}")


def show_banner():
    arquivo = "./resources/banner.txt"

    try:
        with open(arquivo, 'r') as file:
            conteudo = file.read()
            print(conteudo)
    except FileNotFoundError:
        pass
    except Exception as e:
        pass


def init():
    show_banner()
    print("*** Cadastro de usuario ***")
    name = input("Insira o nome do usuario: ")
    return requests.cadastrarCliente(name)


requests = Requests()

if __name__ == '__main__':
    user = init()
    sala  = input("insira o nome da sala: ")
    requests.acessarSala(sala, user)
    requests.sayHello()

