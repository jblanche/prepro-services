# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import image2pose_pb2 as image2pose__pb2


class Image2PoseStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Run = channel.unary_unary(
        '/Image2Pose/Run',
        request_serializer=image2pose__pb2.Image2PoseRequest.SerializeToString,
        response_deserializer=image2pose__pb2.Image2PoseReply.FromString,
        )


class Image2PoseServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Run(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_Image2PoseServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Run': grpc.unary_unary_rpc_method_handler(
          servicer.Run,
          request_deserializer=image2pose__pb2.Image2PoseRequest.FromString,
          response_serializer=image2pose__pb2.Image2PoseReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Image2Pose', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))