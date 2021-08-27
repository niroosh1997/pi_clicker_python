"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc
import changeangle_pb2
import changeangle_pb2_grpc

class ChangeAngle(changeangle_pb2_grpc.ChangeAngleServiceServicer):

    def changeAngle(self, request, context):
        print(request.angle)
        print(f"host is: {context.peer()}")
        # todo: add change angle to servo
        return changeangle_pb2.ChangeAngleReply(message='Change angle accepted')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    changeangle_pb2_grpc.add_ChangeAngleServiceServicer_to_server(ChangeAngle(), server)
    server.add_insecure_port('10.100.102.13:50051')
    server.start()
    print("waiting for termination")
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
