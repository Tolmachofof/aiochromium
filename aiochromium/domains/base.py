import abc
import collections


RequestFrame = collections.namedtuple('RequestFrame', ['method', 'params'])


class Domain:

    @staticmethod
    def create_frame(method, params=None):
        if params is not None:
            params = dict(
                (param, value)
                for param, value in params.items() if value is not None
            )
        return RequestFrame(method, params)


class BaseType(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def from_response(self, response_obj):
        raise NotImplementedError
