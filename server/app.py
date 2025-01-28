from concurrent import futures
import signal
import sys
import grpc
import proto.game_pb2_grpc as game_pb2_grpc
import  proto.game_pb2 as game_pb2
import logging
import secrets

from game.cliente.cliente import Cliente

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class gameSettins():
    def __init__(self, cards_total = 20):
        self.clients = []
        self.rooms = {}
        self.duelos = {}
        self.cards_total = cards_total

    def find_user_by_token(self, token):
        for cliente in self.clients:
            if cliente.chave == token:
                return cliente
        return None

    def find_room_by_name(self, name):
        if name in self.rooms:
            return self.rooms[name]
        return None

    def find_room_by_cliente(self, cliente):
        for room_name, clients in self.rooms.items():
            for c in clients:
                if c.chave == cliente.chave:
                    return room_name
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
                return
        else:
            self.rooms[name] = [c]

        logging.info(f"add client in {name} room")

    def verMao(self, token):
        c = self.find_user_by_token(token)
        if c == None:
            raise ValueError("User not found")
        logging.info(f"Cliente {c.nome} viu sua mao")

        for chave, lista in self.rooms.items():
            if c in lista:
                if len(lista) < 2:
                    return []
                break
        return c.top_deck

    def getCarta(self, token):
        c = self.find_user_by_token(token)
        if c == None:
            raise ValueError("User not found")
        c.get_card()
        logging.info(f"Cliente {c.nome} pegou uma nova carta do jogo")
        return self.verMao(token)

    def desistirJogo(self, token):
        c = self.find_user_by_token(token)
        if c == None:
            raise ValueError("User not found")
        self.clients.remove(c)
        for chave, lista in self.rooms.items():
            if c in lista:
                lista.remove(c)
                break
        logging.info(f"Cliente {c.nome} saiu do jogo")

    def jogar(self, token, idx):
        c = self.find_user_by_token(token)
        if c == None:
            raise ValueError("User not found")
        carta = c.joga_carta(idx)
        if carta == None:
            self.desistirJogo(token)
            return None
        room = self.find_room_by_cliente(c)
        if room in self.duelos:
            self.duelos[room].append(carta)
        else:
            self.duelos[room] = [carta]

        while len(self.duelos[room]) < 2:
            pass

        cp = self.duelos[room].copy()
        cp.remove(carta)

        c1 = cp[0]

        return carta.attack_outher_card(c1)

    def clean_duelos(self, room_name):
        if len( self.duelos[room_name]) ==2:
            self.duelos[room_name] = []

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

        opoString = None
        if(completed):
            c = self.game.find_user_by_token(request.token)
            opo = None

            if room[0].chave == request.token:
                opo = room[1]
            else:
                opo = room[0]

            if(opo != None):
                opoString = opo.nome
        return game_pb2.SalaResponse(finalizada=completed, message = message, erro=False, oponente= opoString )

    def verMao(self, request, context):
            cards = self.game.verMao(request.string)
            return game_pb2.CartasResponse(cartas=[str(card) for card in cards])

    def pegarCartaDeck(self, request, context):
            cards = self.game.getCarta(request.string)
            return game_pb2.CartasResponse(cartas=[str(card) for card in cards])

    def desistirJogo(self, request, context):
        try:
            self.game.desistirJogo(request.string)
        except Exception as e:
            return game_pb2.boolResponse(resp=False)
        return game_pb2.boolResponse(resp=True)

    def jogar(self, request, context):
        rsesp = self.game.jogar(request.string, request.idx)
        if(rsesp == None):
            return game_pb2.JogarResponse(tuple="sem mais cartas =(", victory = False, draw = False)
        return game_pb2.JogarResponse(tuple=str(rsesp), victory = rsesp.is_victory(), draw = rsesp.is_draw())

    def clean_duelo(self, request, context):
        self.game.clean_duelos(request.string)
        return game_pb2.boolResponse(resp=True)


def signal_handler(sig, frame):
    """Lidar com a interrupção do servidor"""
    print("\nRecebido sinal de interrupção (Ctrl+Z ou Ctrl+C). Finalizando servidor...")
    server.stop(0)  # Interrompe o servidor
    sys.exit(0)  # Finaliza o processo

def serve(gam, end, porta):
    global server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    game_pb2_grpc.add_GameServiceServicer_to_server(GameServiceServicer(game), server)
    server.add_insecure_port(f'{end}:{porta}')

    # Configurar o sinal de interrupção (Ctrl+Z ou Ctrl+C)
    signal.signal(signal.SIGINT, signal_handler)  # Captura Ctrl+C
    signal.signal(signal.SIGTSTP, signal_handler)  # Captura Ctrl+Z

    logging.info(f"Servidor rodando em {end}:{porta}...")
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
    if len(sys.argv) < 2:
        end = '127.0.0.1'
    else:
        end = sys.argv[1]
    if len(sys.argv) < 3:
        porta = 50051
    else:
        porta = int(sys.argv[2])

    game = init()
    serve(game, end, porta)
