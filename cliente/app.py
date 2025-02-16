import grpc
import proto.game_pb2_grpc as game_pb2_grpc
import  proto.game_pb2 as game_pb2
from user.User import User
import sys

ganhou = 0
perdeu = 0
oponente = None
class Requests():
    def __init__(self, end, porta):
        self.empty = game_pb2.google_dot_protobuf_dot_empty__pb2.Empty()

    def get_target(self):
        return f"{end}:{porta}"

    def sayHello(self):
        with grpc.insecure_channel(self.get_target(), options=(('grpc.enable_http_proxy', 0), ('grpc.default_authority', 'localhost'))) as channel:
            self.stub = game_pb2_grpc.GameServiceStub(channel)
            response = self.stub.sayHello(self.empty)
            print(f"Resposta do servidor: {response.string}")

    def cadastrarCliente(self, name):
        with grpc.insecure_channel(self.get_target(), options=(('grpc.enable_http_proxy', 0), ('grpc.default_authority', 'localhost'))) as channel:
            self.stub = game_pb2_grpc.GameServiceStub(channel)
            stringRequest = game_pb2.StringRequest(string=name)
            response = self.stub.cadastrarCliente(stringRequest)
            user = User(name=response.name, chave=response.chave)
            print(f"Usuário {response.name} cadastrado com sucesso!!!")
            return user

    def acessarSala(self, name, user):
        with grpc.insecure_channel(self.get_target(), options=(('grpc.enable_http_proxy', 0), ('grpc.default_authority', 'localhost'))) as channel:
            self.stub = game_pb2_grpc.GameServiceStub(channel)
            salaRequest = game_pb2.SalaRequest(name = name,token = user.chave)
            return self.stub.acessarSala(salaRequest)

    def verMao(self, user):
        with grpc.insecure_channel(self.get_target(), options=(('grpc.enable_http_proxy', 0), ('grpc.default_authority', 'localhost'))) as channel:
            self.stub = game_pb2_grpc.GameServiceStub(channel)
            stringRequest = game_pb2.StringRequest(string = user.chave)
            return self.stub.verMao(stringRequest).cartas

    def pegarCartaDeck(self, user):
        with grpc.insecure_channel(self.get_target(), options=(('grpc.enable_http_proxy', 0), ('grpc.default_authority', 'localhost'))) as channel:
            self.stub = game_pb2_grpc.GameServiceStub(channel)
            stringRequest = game_pb2.StringRequest(string = user.chave)
            response = self.stub.pegarCartaDeck(stringRequest)
            print(f"voce pegou a carta: {response.cartas[len(response.cartas)-1]}")

    def jogar(self, user, idx):
        with grpc.insecure_channel(self.get_target(), options=(('grpc.enable_http_proxy', 0), ('grpc.default_authority', 'localhost'))) as channel:
            if(idx > user.cartas or idx < 0):
                print("index errado")
                return
            self.stub = game_pb2_grpc.GameServiceStub(channel)
            stringRequest = game_pb2.JogarRequest(idx = idx, string = user.chave)
            return self.stub.jogar(stringRequest)

    def clean_duelo(self, sala):
        with grpc.insecure_channel(self.get_target(), options=(('grpc.enable_http_proxy', 0), ('grpc.default_authority', 'localhost'))) as channel:
            self.stub = game_pb2_grpc.GameServiceStub(channel)
            stringRequest = game_pb2.StringRequest(string = sala)
            return self.stub.clean_duelo(stringRequest)

    def desistirJogo(self, user):
        with grpc.insecure_channel(self.get_target(), options=(('grpc.enable_http_proxy', 0), ('grpc.default_authority', 'localhost'))) as channel:
            self.stub = game_pb2_grpc.GameServiceStub(channel)
            stringRequest = game_pb2.StringRequest(string = user.chave)
            response = self.stub.desistirJogo(stringRequest)
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

def check_final():
    if user.cartas == 0:
        if ganhou > perdeu:
            print(f"parabens vc ganhou de {oponente}")
        elif ganhou < perdeu:
            print(f"infelizmente vc perdeu para {oponente}")
        else:
            print(f"vc empatou {oponente} :o ")
        requests.desistirJogo(user)
        return True
    return False

def show_menu(user):
    global ganhou
    global perdeu
    global acabou
    acabou = False
    cartas = requests.verMao(user)
    user.cartas = len(cartas)
    while(not acabou):
        print(f"USER {user.name}: vitorias => {ganhou} derrotas => {perdeu}")
        print("1- ver mao")
        print("2- pegar carta do deck")
        print("3- sair jogo")
        item = int(input("> "))

        if item == 1:
            cartas = requests.verMao(user)
            user.cartas = len(cartas)

            acabou = check_final()

            for i, carta in enumerate(cartas):
                print(f"{i}. {carta}")
            print(len(cartas), '. sair')

            op = int(input("> "))

            if op == len(cartas):
                continue

            print("espere...")
            resp =  requests.jogar(user, op)

            if(resp == None):
                continue
            print(resp.tuple)
            user.cartas = user.cartas - 1


            if resp.draw:
                print("EMPATE")
            elif resp.victory:
                print(f"voce ganhou essa rodada !!!")
                ganhou = ganhou + 1
            else:
                print(f"voce perdeu essa rodada. {oponente} ganhou !!!")
                perdeu = perdeu + 1
            requests.clean_duelo(sala)
            acabou = check_final()

        elif item == 2:
            if user.cartas > 0:
                requests.pegarCartaDeck(user)
                user.cartas = user.cartas + 1
            else:
                acabou = check_final()
        elif item == 3:
            requests.desistirJogo(user)
            user.cartas = 0
            acabou = True
            print("bye")
            break
    return None


def init(end, porta):
    show_banner()
    global requests
    requests = Requests(end, porta)
    print("*** Cadastro de usuario ***")
    name = input("Insira o nome do usuario: ")
    return requests.cadastrarCliente(name)




if __name__ == '__main__':
    if len(sys.argv) < 2:
        end = '127.0.0.1'
    else:
        end = sys.argv[1]
    if len(sys.argv) < 3:
        porta = 50051
    else:
        porta = int(sys.argv[2])

    user = init(end, porta)
    requests.sayHello()

    while True:
        global sala
        sala  = input("insira o nome da sala: ")
        print("espere...")

        sala_fechada = None

        while sala_fechada == None or not sala_fechada.finalizada:
            sala_fechada = requests.acessarSala(sala, user)
            if sala_fechada.erro:
                print("sala em uso tente outra sala")
                break
        if not sala_fechada.erro:
            oponente = sala_fechada.oponente
            print(f"seu oponente {oponente} entrou na sala")
            break

    show_menu(user)


