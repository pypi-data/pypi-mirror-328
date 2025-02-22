from setuptools import setup, find_packages

setup(
    name="grpc_protos",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["grpcio", "protobuf"],
)
