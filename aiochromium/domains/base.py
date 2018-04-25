import abc
import collections
from functools import partial


RequestFrame = collections.namedtuple(
    'RequestFrame', ['domain_method', 'params', 'wrapper_class']
)


class BaseDomain:

    @staticmethod
    def create_frame(
        domain_method, params=None, wrapper_class=None, source=None,
        target=None
    ):
        if params is not None:
            params = dict(
                (param, value)
                for param, value in params.items() if value is not None
            )
        if wrapper_class is not None:
            wrapper_class = partial(
                wrapper_class.from_response, source=source, target=target
            )
        return RequestFrame(domain_method, params, wrapper_class)


class BaseEvent:
    pass


class BaseType(metaclass=abc.ABCMeta):

    @classmethod
    @abc.abstractmethod
    def to_internal(cls, item, blank=False, **kwargs):
        raise NotImplementedError

    @classmethod
    def from_response(
        cls, response_obj, blank=False, default=None, source=None, **kwargs
    ):
        if response_obj:
            if source is None:
                return cls.to_internal(response_obj, **kwargs)
            elif source in response_obj:
                return cls.to_internal(response_obj[source])
            elif blank:
                return default
        else:
            if blank:
                return default
            else:
                raise ValueError

    @classmethod
    def _get_optional(cls, response_obj, name, wrapper=None, default=None):
        if name in response_obj:
            return (
                wrapper(response_obj[name])
                if wrapper is not None else response_obj[name]
            )
        return default


class String(BaseType):

    @classmethod
    def to_internal(cls, item, **kwargs):
        return str(item)


class Integer(BaseType):

    @classmethod
    def to_internal(cls, item, blank=False, **kwargs):
        return int(item)


class Array(BaseType):

    @classmethod
    def to_internal(cls, items, blank=False, target=None):
        if target is not None:
            return [target.to_internal(item) for item in items]
        else:
            return items
