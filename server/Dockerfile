# Usar a imagem oficial do Python como base
FROM python:3.11-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar os arquivos para o diretório de trabalho no contêiner
COPY . .

# Instalar as dependências diretamente a partir do requirements.txt
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

RUN pip install --upgrade protobuf

RUN  python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. ./proto/game.proto


# Expor a porta usada pela aplicação
EXPOSE 50051

# Comando para executar o app
CMD ["python", "app.py"]
