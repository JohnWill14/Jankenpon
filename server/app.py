from concurrent import futures
from weakref import finalize

import grpc
import proto.game_pb2_grpc as game_pb2_grpc
import  proto.game_pb2 as game_pb2
import logging
import secrets

from cliente.cliente import Cliente

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class gameSettins():
    def __init__(self):
        self.clients = []
        self.rooms = {}

    def find_user_by_token(self, token):
        for cliente in self.clients:
            if cliente.chave == token:
                return cliente
        return None

    def find_room_by_name(self, name):
        if name in self.rooms:
            return self.rooms[name]
        return None

    def addClient(self, name):
        token = secrets.token_hex(16)
        c = Cliente(name, token)
        self.clients.append(c)
        return c

    def addRoom(self, name, token):
        c = self.find_user_by_token(token)
        if c == None:
            raise ValueError("User not found")

        if name in self.rooms:
            if c not in self.rooms[name]:
                if len(self.rooms[name]) < 2:
                    self.rooms[name].append(c)
                else:
                    raise ValueError("Room is closed")
        else:
            self.rooms[name] = [c]

        logging.info(f"add client in {name} room")


class GameServiceServicer(game_pb2_grpc.GameServiceServicer):
    def __init__(self, gameSettins):
        self.game = gameSettins

    def sayHello(self, request, context):
        return game_pb2.StringRequest(string="Olá! Bem-vindo ao servidor Jankenpom gRPC.")

    def cadastrarCliente(self, request, context):
        cliente = self.game.addClient(request.string)

        logging.info(f"add client  {cliente.nome}")
        return game_pb2.ClienteResponse(name=cliente.nome, chave=cliente.chave)

    def acessarSala(self, request, context):
        try:
            self.game.addRoom(request.name, request.token)
        except Exception as e:
            logging.info(f"Erro: {e}")
            return game_pb2.SalaResponse(finalizada=True, message=str(e), erro = True)

        room = self.game.find_room_by_name(request.name)

        completed = len(room) == 2
        message = "OK" if completed else "Wait pls"

        return game_pb2.SalaResponse(finalizada=completed, message = message, erro=False)



def serve(game):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    game_pb2_grpc.add_GameServiceServicer_to_server(GameServiceServicer(game), server)
    server.add_insecure_port('127.0.0.1:50051')
    logging.info("Servidor rodando na porta 50051...")
    server.start()
    server.wait_for_termination()


def show_banner():
    arquivo = "./resources/banner.txt"

    try:
        with open(arquivo, 'r') as file:
            conteudo = file.read()
            print(conteudo)
            print()
    except FileNotFoundError:
        pass
    except Exception as e:
        pass


def init():
    show_banner()
    return gameSettins()

if __name__ == "__main__":
    game = init()
    serve(game)
