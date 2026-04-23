# Backend Proto Update and Regeneration

Use this when proto contracts change and backend gRPC Python files must be regenerated.


From `cipherconverter-backend` root:

```bash
make update-proto
make proto
```

Optional one-liner:

```bash
make all
```

## Verify

```bash
make verify
```

Generated files are in `cipherconverter/ciphers/grpc`.

Note: `make proto` also patches generated imports to package-relative form and removes old `cipher_pb2*` files.

If you also updated the submodule pointer, check:

```bash
git -C ../cipherconverter-microservice status
```