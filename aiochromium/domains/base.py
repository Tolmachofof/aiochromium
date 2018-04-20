import abc
import collections


RequestFrame = collections.namedtuple(
    'RequestFrame', ['domain_method', 'params', 'wrapper_class']
)


class Domain:

    @staticmethod
    def create_frame(domain_method, params=None, wrapper_class=None):
        if params is not None:
            params = dict(
                (param, value)
                for param, value in params.items() if value is not None
            )
        return RequestFrame(domain_method, params, wrapper_class)


class BaseType(metaclass=abc.ABCMeta):

    def __new__(cls, response_obj, source=None, **kwargs):
        return cls.from_response(response_obj, source, **kwargs)

    @classmethod
    @abc.abstractmethod
    def to_internal(cls, item, **kwargs):
        raise NotImplementedError

    @classmethod
    def from_response(cls, response_obj, source=None, **kwargs):
        if source is None:
            return cls.to_internal(response_obj, **kwargs)
        elif source in response_obj:
            return cls.to_internal(response_obj[source])


class String(BaseType):

    @classmethod
    def to_internal(cls, item, **kwargs):
        return str(item)


class Integer(BaseType):

    @classmethod
    def to_internal(cls, item, **kwargs):
        return int(item)


class Array(BaseType):

    @classmethod
    def to_internal(cls, items, target=None):
        if target is not None:
            return [target(item) for item in items]
        else:
            return items
