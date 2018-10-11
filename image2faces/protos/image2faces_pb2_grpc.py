# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import image2faces_pb2 as image2faces__pb2


class Image2FacesStub(object):
  """The service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Run = channel.unary_unary(
        '/Image2Faces/Run',
        request_serializer=image2faces__pb2.Image2FacesRequest.SerializeToString,
        response_deserializer=image2faces__pb2.Image2FacesReply.FromString,
        )


class Image2FacesServicer(object):
  """The service definition.
  """

  def Run(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_Image2FacesServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Run': grpc.unary_unary_rpc_method_handler(
          servicer.Run,
          request_deserializer=image2faces__pb2.Image2FacesRequest.FromString,
          response_serializer=image2faces__pb2.Image2FacesReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Image2Faces', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
