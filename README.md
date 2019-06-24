# py-gRPC

 
#### Generate rpc stubs
1. git clone https://github.com/googleapis/googleapis repo outside your project repo, say ../../external folder
2. run: 
        python -m grpc_tools.protoc --proto_path=../../external/googleapis:. --python_out=../common --grpc_python_out=../common digestor.proto
3. it will generate stubs in your projects ./common folder