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
        return RequestFrame(domain_method, params, wrapper_class)


class BaseEvent:
    pass


class BaseField:

    def __init__(self, source=None, blank=False, default=None):
        self._source = source
        self._blank = blank
        self._default = default

    @property
    def source(self):
        return self._source

    @property
    def blank(self):
        return self._blank

    @property
    def default(self):
        return self._default

    def to_internal(self, item):
        raise NotImplementedError

    def from_response(self, response_obj):
        if self._source is None:
            return self.to_internal(response_obj)
        elif response_obj and self._source in response_obj:
            return self.to_internal(response_obj[self._source])
        elif self._blank:
            return self._default
        else:
            raise AttributeError


class Integer(BaseField):

    def to_internal(self, item):
        return int(item)


class String(BaseField):

    def to_internal(self, item):
        return str(item)


class Array(BaseField):

    def __init__(self, source=None, target=None, blank=False, default=None):
        super().__init__(source, blank, default)
        self._target = target

    @property
    def target(self):
        return self._target

    def to_internal(self, items):
        if self._target is not None:
            return [self._target().to_internal(item) for item in items]
        else:
            return list(items)


class ObjectMeta(type):

    def __new__(mcs, name, bases, attrs):
        new_class = super().__new__(mcs, name, bases, attrs)
        new_class._fields = []
        for field, value in attrs.items():
            if not (field.startswith('__') and field.endswith('__')):
                new_class.add_to_class(field, value)
        return new_class

    def add_to_class(cls, field_name, field_value):
        cls._fields.append(field_name)
        if hasattr(field_value, 'target') and field_value.target == 'self':
            field_value.__dict__['_target'] = cls
        setattr(cls, field_name, field_value)


class BaseObject(BaseField, metaclass=ObjectMeta):

    def to_internal(self, item):
        for field_name in self._fields:
            field = getattr(self, field_name)
            setattr(self, field_name, field.from_response(item))
        return self

