import abc
import collections

from ..utils.naming_transformer import (
    camel_case_to_snake_case, snake_case_to_camel_case
)


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

    OPTIONAL_ARGS = ()

    def __init__(self, *args, **kwargs):
        for optional_arg in self.OPTIONAL_ARGS:
            pass


    @abc.abstractmethod
    def from_response(self, executor, response_obj):
        raise NotImplementedError
