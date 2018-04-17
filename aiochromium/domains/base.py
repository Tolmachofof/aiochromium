import abc
import collections


DomainMethod = collections.namedtuple(
    'DomainMethod', ['method', 'wrapper_class']
)


RequestFrame = collections.namedtuple(
    'RequestFrame', ['domain_method', 'params']
)


class Domain:

    @staticmethod
    def create_frame(domain_method, params=None):
        if params is not None:
            params = dict(
                (param, value)
                for param, value in params.items() if value is not None
            )
        return RequestFrame(domain_method, params)


class BaseType(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def from_response(self, executor, response_obj):
        raise NotImplementedError
