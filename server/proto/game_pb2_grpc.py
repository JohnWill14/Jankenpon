# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from proto import game_pb2 as proto_dot_game__pb2

GRPC_GENERATED_VERSION = '1.69.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in proto/game_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class GameServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.sayHello = channel.unary_unary(
                '/GameService/sayHello',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=proto_dot_game__pb2.StringRequest.FromString,
                _registered_method=True)
        self.cadastrarCliente = channel.unary_unary(
                '/GameService/cadastrarCliente',
                request_serializer=proto_dot_game__pb2.StringRequest.SerializeToString,
                response_deserializer=proto_dot_game__pb2.ClienteResponse.FromString,
                _registered_method=True)
        self.acessarSala = channel.unary_unary(
                '/GameService/acessarSala',
                request_serializer=proto_dot_game__pb2.SalaRequest.SerializeToString,
                response_deserializer=proto_dot_game__pb2.SalaResponse.FromString,
                _registered_method=True)
        self.verMao = channel.unary_unary(
                '/GameService/verMao',
                request_serializer=proto_dot_game__pb2.StringRequest.SerializeToString,
                response_deserializer=proto_dot_game__pb2.CartasResponse.FromString,
                _registered_method=True)
        self.jogar = channel.unary_unary(
                '/GameService/jogar',
                request_serializer=proto_dot_game__pb2.JogarRequest.SerializeToString,
                response_deserializer=proto_dot_game__pb2.JogarResponse.FromString,
                _registered_method=True)
        self.pegarCartaDeck = channel.unary_unary(
                '/GameService/pegarCartaDeck',
                request_serializer=proto_dot_game__pb2.StringRequest.SerializeToString,
                response_deserializer=proto_dot_game__pb2.CartasResponse.FromString,
                _registered_method=True)
        self.desistirJogo = channel.unary_unary(
                '/GameService/desistirJogo',
                request_serializer=proto_dot_game__pb2.StringRequest.SerializeToString,
                response_deserializer=proto_dot_game__pb2.boolResponse.FromString,
                _registered_method=True)
        self.clean_duelo = channel.unary_unary(
                '/GameService/clean_duelo',
                request_serializer=proto_dot_game__pb2.StringRequest.SerializeToString,
                response_deserializer=proto_dot_game__pb2.boolResponse.FromString,
                _registered_method=True)


class GameServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def sayHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def cadastrarCliente(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def acessarSala(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def verMao(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def jogar(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def pegarCartaDeck(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def desistirJogo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def clean_duelo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GameServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'sayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.sayHello,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=proto_dot_game__pb2.StringRequest.SerializeToString,
            ),
            'cadastrarCliente': grpc.unary_unary_rpc_method_handler(
                    servicer.cadastrarCliente,
                    request_deserializer=proto_dot_game__pb2.StringRequest.FromString,
                    response_serializer=proto_dot_game__pb2.ClienteResponse.SerializeToString,
            ),
            'acessarSala': grpc.unary_unary_rpc_method_handler(
                    servicer.acessarSala,
                    request_deserializer=proto_dot_game__pb2.SalaRequest.FromString,
                    response_serializer=proto_dot_game__pb2.SalaResponse.SerializeToString,
            ),
            'verMao': grpc.unary_unary_rpc_method_handler(
                    servicer.verMao,
                    request_deserializer=proto_dot_game__pb2.StringRequest.FromString,
                    response_serializer=proto_dot_game__pb2.CartasResponse.SerializeToString,
            ),
            'jogar': grpc.unary_unary_rpc_method_handler(
                    servicer.jogar,
                    request_deserializer=proto_dot_game__pb2.JogarRequest.FromString,
                    response_serializer=proto_dot_game__pb2.JogarResponse.SerializeToString,
            ),
            'pegarCartaDeck': grpc.unary_unary_rpc_method_handler(
                    servicer.pegarCartaDeck,
                    request_deserializer=proto_dot_game__pb2.StringRequest.FromString,
                    response_serializer=proto_dot_game__pb2.CartasResponse.SerializeToString,
            ),
            'desistirJogo': grpc.unary_unary_rpc_method_handler(
                    servicer.desistirJogo,
                    request_deserializer=proto_dot_game__pb2.StringRequest.FromString,
                    response_serializer=proto_dot_game__pb2.boolResponse.SerializeToString,
            ),
            'clean_duelo': grpc.unary_unary_rpc_method_handler(
                    servicer.clean_duelo,
                    request_deserializer=proto_dot_game__pb2.StringRequest.FromString,
                    response_serializer=proto_dot_game__pb2.boolResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'GameService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('GameService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class GameService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def sayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/GameService/sayHello',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            proto_dot_game__pb2.StringRequest.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def cadastrarCliente(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/GameService/cadastrarCliente',
            proto_dot_game__pb2.StringRequest.SerializeToString,
            proto_dot_game__pb2.ClienteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def acessarSala(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/GameService/acessarSala',
            proto_dot_game__pb2.SalaRequest.SerializeToString,
            proto_dot_game__pb2.SalaResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def verMao(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/GameService/verMao',
            proto_dot_game__pb2.StringRequest.SerializeToString,
            proto_dot_game__pb2.CartasResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def jogar(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/GameService/jogar',
            proto_dot_game__pb2.JogarRequest.SerializeToString,
            proto_dot_game__pb2.JogarResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def pegarCartaDeck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/GameService/pegarCartaDeck',
            proto_dot_game__pb2.StringRequest.SerializeToString,
            proto_dot_game__pb2.CartasResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def desistirJogo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/GameService/desistirJogo',
            proto_dot_game__pb2.StringRequest.SerializeToString,
            proto_dot_game__pb2.boolResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def clean_duelo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/GameService/clean_duelo',
            proto_dot_game__pb2.StringRequest.SerializeToString,
            proto_dot_game__pb2.boolResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
