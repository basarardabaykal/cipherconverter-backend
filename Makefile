.PHONY: proto-tools update-proto proto verify clean-proto all

PYTHON ?= python
MICROSERVICE_DIR ?= ../cipherconverter-microservice
PROTO_DIR ?= $(MICROSERVICE_DIR)/proto
GRPC_DIR ?= ./cipherconverter/ciphers/grpc

all: update-proto proto

proto-tools:
	@echo "Installing grpcio-tools..."
	$(PYTHON) -m pip install grpcio-tools==1.71.0

update-proto:
	@echo "Updating proto submodule in microservice..."
	git -C $(MICROSERVICE_DIR) submodule update --init --remote --merge proto

proto: proto-tools
	@echo "Generating Python gRPC files for backend..."
	$(PYTHON) -m grpc_tools.protoc \
		-I $(PROTO_DIR) \
		--python_out=$(GRPC_DIR) \
		--pyi_out=$(GRPC_DIR) \
		--grpc_python_out=$(GRPC_DIR) \
		$(PROTO_DIR)/common.proto \
		$(PROTO_DIR)/symmetric.proto
	@# grpc_tools emits top-level imports; convert to package-relative imports.
	perl -i -pe 's/^import common_pb2 as /from . import common_pb2 as /' $(GRPC_DIR)/symmetric_pb2.py
	perl -i -pe 's/^import common_pb2 as /from . import common_pb2 as /' $(GRPC_DIR)/symmetric_pb2_grpc.py
	perl -i -pe 's/^import symmetric_pb2 as /from . import symmetric_pb2 as /' $(GRPC_DIR)/symmetric_pb2_grpc.py
	@# Remove obsolete files from old cipher.proto contract.
	rm -f $(GRPC_DIR)/cipher_pb2.py $(GRPC_DIR)/cipher_pb2.pyi $(GRPC_DIR)/cipher_pb2_grpc.py
	@echo "Done. Generated files are in $(GRPC_DIR)."

verify:
	git diff -- $(GRPC_DIR)

clean-proto:
	@echo "Cleaning generated protobuf files..."
	rm -f $(GRPC_DIR)/common_pb2.py \
		$(GRPC_DIR)/common_pb2.pyi \
		$(GRPC_DIR)/common_pb2_grpc.py \
		$(GRPC_DIR)/symmetric_pb2.py \
		$(GRPC_DIR)/symmetric_pb2.pyi \
		$(GRPC_DIR)/symmetric_pb2_grpc.py