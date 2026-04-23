# Backend Proto Update and Regeneration

Use this when proto contracts change and backend gRPC Python files must be regenerated.

## 1. Update proto submodule to latest

From workspace root:

```bash
cd cipherconverter-microservice
git submodule update --init --remote --merge proto
```

## 2. Generate backend Python gRPC files

From workspace root:

```bash
cd cipherconverter-backend
python -m pip install grpcio-tools==1.71.0

python -m grpc_tools.protoc \
  -I ../cipherconverter-microservice/proto \
  --python_out=./cipherconverter/ciphers/grpc \
  --pyi_out=./cipherconverter/ciphers/grpc \
  --grpc_python_out=./cipherconverter/ciphers/grpc \
  ../cipherconverter-microservice/proto/common.proto \
  ../cipherconverter-microservice/proto/symmetric.proto
```

This regenerates:
- `cipherconverter/ciphers/grpc/common_pb2.py`
- `cipherconverter/ciphers/grpc/common_pb2.pyi`
- `cipherconverter/ciphers/grpc/common_pb2_grpc.py`
- `cipherconverter/ciphers/grpc/symmetric_pb2.py`
- `cipherconverter/ciphers/grpc/symmetric_pb2.pyi`
- `cipherconverter/ciphers/grpc/symmetric_pb2_grpc.py`

## 3. Verify

```bash
git diff -- cipherconverter/ciphers/grpc
```

If you also updated the submodule pointer, check:

```bash
git -C ../cipherconverter-microservice status
```