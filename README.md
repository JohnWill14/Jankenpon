# Autores

  * Gabriel Valentim De Oliveira Dacie
  * John William Vicente 

# Run

```bash
  cd ./cliente
  python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. ./proto/game.proto
  cd ..
  cd server
  python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. ./proto/game.proto
 ```



```bash
  cd server
  python app.py
  cd ..
  cd ./cliente
  python app.py  
  ```
