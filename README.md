# pi_clicker_python
Python server that will be on pi and will mechanical click with servo


To generate .py files of protobuf: "changeangle.proto", use command:
```shell
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./changeangle.proto
```