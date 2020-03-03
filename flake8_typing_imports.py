import ast
import collections
import configparser
import os.path
import sys
from typing import Any
from typing import Dict
from typing import Generator
from typing import List
from typing import NamedTuple
from typing import Set
from typing import Tuple
from typing import Type

if sys.version_info < (3, 8):  # pragma: no cover (<PY38)
    import importlib_metadata
else:  # pragma: no cover (PY38+)
    import importlib.metadata as importlib_metadata


class Version(NamedTuple):
    major: int = 0
    minor: int = 0
    patch: int = 0

    def __str__(self) -> str:
        return f'{self.major}.{self.minor}.{self.patch}'

    @classmethod
    def parse(cls, s: str) -> 'Version':
        return cls(*[int(p) for p in s.split('.')])


# GENERATED BY ./bin/build-generated
SYMBOLS = (
    (
        Version(3, 5, 0), frozenset((
            'AbstractSet', 'Any', 'AnyStr', 'BinaryIO', 'ByteString',
            'Callable', 'Container', 'Dict', 'FrozenSet', 'Generator',
            'Generic', 'Hashable', 'IO', 'ItemsView', 'Iterable', 'Iterator',
            'KeysView', 'List', 'Mapping', 'MappingView', 'Match',
            'MutableMapping', 'MutableSequence', 'MutableSet', 'NamedTuple',
            'Optional', 'Pattern', 'Reversible', 'Sequence', 'Set', 'Sized',
            'SupportsAbs', 'SupportsBytes', 'SupportsComplex', 'SupportsFloat',
            'SupportsInt', 'SupportsRound', 'TextIO', 'Tuple', 'TypeVar',
            'Union', 'ValuesView', 'cast', 'get_type_hints', 'no_type_check',
            'no_type_check_decorator', 'overload',
        )),
    ),
    (
        Version(3, 5, 1), frozenset((
            'AbstractSet', 'Any', 'AnyStr', 'BinaryIO', 'ByteString',
            'Callable', 'Container', 'Dict', 'FrozenSet', 'Generator',
            'Generic', 'Hashable', 'IO', 'ItemsView', 'Iterable', 'Iterator',
            'KeysView', 'List', 'Mapping', 'MappingView', 'Match',
            'MutableMapping', 'MutableSequence', 'MutableSet', 'NamedTuple',
            'Optional', 'Pattern', 'Reversible', 'Sequence', 'Set', 'Sized',
            'SupportsAbs', 'SupportsBytes', 'SupportsComplex', 'SupportsFloat',
            'SupportsInt', 'SupportsRound', 'TextIO', 'Tuple', 'TypeVar',
            'Union', 'ValuesView', 'cast', 'get_type_hints', 'no_type_check',
            'no_type_check_decorator', 'overload',
        )),
    ),
    (
        Version(3, 5, 2), frozenset((
            'AbstractSet', 'Any', 'AnyStr', 'AsyncIterable', 'AsyncIterator',
            'Awaitable', 'BinaryIO', 'ByteString', 'Callable', 'Container',
            'DefaultDict', 'Dict', 'FrozenSet', 'Generator', 'Generic',
            'Hashable', 'IO', 'ItemsView', 'Iterable', 'Iterator', 'KeysView',
            'List', 'Mapping', 'MappingView', 'Match', 'MutableMapping',
            'MutableSequence', 'MutableSet', 'NamedTuple', 'NewType',
            'Optional', 'Pattern', 'Reversible', 'Sequence', 'Set', 'Sized',
            'SupportsAbs', 'SupportsBytes', 'SupportsComplex', 'SupportsFloat',
            'SupportsInt', 'SupportsRound', 'TYPE_CHECKING', 'Text', 'TextIO',
            'Tuple', 'Type', 'TypeVar', 'Union', 'ValuesView', 'cast',
            'get_type_hints', 'no_type_check', 'no_type_check_decorator',
            'overload',
        )),
    ),
    (
        Version(3, 5, 3), frozenset((
            'AbstractSet', 'Any', 'AnyStr', 'AsyncIterable', 'AsyncIterator',
            'Awaitable', 'BinaryIO', 'ByteString', 'Callable', 'ClassVar',
            'Container', 'Coroutine', 'DefaultDict', 'Dict', 'FrozenSet',
            'Generator', 'Generic', 'Hashable', 'IO', 'ItemsView', 'Iterable',
            'Iterator', 'KeysView', 'List', 'Mapping', 'MappingView', 'Match',
            'MutableMapping', 'MutableSequence', 'MutableSet', 'NamedTuple',
            'NewType', 'Optional', 'Pattern', 'Reversible', 'Sequence', 'Set',
            'Sized', 'SupportsAbs', 'SupportsBytes', 'SupportsComplex',
            'SupportsFloat', 'SupportsInt', 'SupportsRound', 'TYPE_CHECKING',
            'Text', 'TextIO', 'Tuple', 'Type', 'TypeVar', 'Union',
            'ValuesView', 'cast', 'get_type_hints', 'no_type_check',
            'no_type_check_decorator', 'overload',
        )),
    ),
    (
        Version(3, 5, 4), frozenset((
            'AbstractSet', 'Any', 'AnyStr', 'AsyncContextManager',
            'AsyncIterable', 'AsyncIterator', 'Awaitable', 'BinaryIO',
            'ByteString', 'Callable', 'ChainMap', 'ClassVar', 'Container',
            'ContextManager', 'Coroutine', 'Counter', 'DefaultDict', 'Deque',
            'Dict', 'FrozenSet', 'Generator', 'Generic', 'GenericMeta',
            'Hashable', 'IO', 'ItemsView', 'Iterable', 'Iterator', 'KeysView',
            'List', 'Mapping', 'MappingView', 'Match', 'MutableMapping',
            'MutableSequence', 'MutableSet', 'NamedTuple', 'NewType',
            'NoReturn', 'Optional', 'Pattern', 'Reversible', 'Sequence', 'Set',
            'Sized', 'SupportsAbs', 'SupportsBytes', 'SupportsComplex',
            'SupportsFloat', 'SupportsInt', 'SupportsRound', 'TYPE_CHECKING',
            'Text', 'TextIO', 'Tuple', 'Type', 'TypeVar', 'Union',
            'ValuesView', 'cast', 'get_type_hints', 'no_type_check',
            'no_type_check_decorator', 'overload',
        )),
    ),
    (
        Version(3, 5, 5), frozenset((
            'AbstractSet', 'Any', 'AnyStr', 'AsyncContextManager',
            'AsyncIterable', 'AsyncIterator', 'Awaitable', 'BinaryIO',
            'ByteString', 'Callable', 'ChainMap', 'ClassVar', 'Container',
            'ContextManager', 'Coroutine', 'Counter', 'DefaultDict', 'Deque',
            'Dict', 'FrozenSet', 'Generator', 'Generic', 'GenericMeta',
            'Hashable', 'IO', 'ItemsView', 'Iterable', 'Iterator', 'KeysView',
            'List', 'Mapping', 'MappingView', 'Match', 'MutableMapping',
            'MutableSequence', 'MutableSet', 'NamedTuple', 'NewType',
            'NoReturn', 'Optional', 'Pattern', 'Reversible', 'Sequence', 'Set',
            'Sized', 'SupportsAbs', 'SupportsBytes', 'SupportsComplex',
            'SupportsFloat', 'SupportsInt', 'SupportsRound', 'TYPE_CHECKING',
            'Text', 'TextIO', 'Tuple', 'Type', 'TypeVar', 'Union',
            'ValuesView', 'cast', 'get_type_hints', 'no_type_check',
            'no_type_check_decorator', 'overload',
        )),
    ),
    (
        Version(3, 5, 6), frozenset((
            'AbstractSet', 'Any', 'AnyStr', 'AsyncContextManager',
            'AsyncIterable', 'AsyncIterator', 'Awaitable', 'BinaryIO',
            'ByteString', 'Callable', 'ChainMap', 'ClassVar', 'Container',
            'ContextManager', 'Coroutine', 'Counter', 'DefaultDict', 'Deque',
            'Dict', 'FrozenSet', 'Generator', 'Generic', 'GenericMeta',
            'Hashable', 'IO', 'ItemsView', 'Iterable', 'Iterator', 'KeysView',
            'List', 'Mapping', 'MappingView', 'Match', 'MutableMapping',
            'MutableSequence', 'MutableSet', 'NamedTuple', 'NewType',
            'NoReturn', 'Optional', 'Pattern', 'Reversible', 'Sequence', 'Set',
            'Sized', 'SupportsAbs', 'SupportsBytes', 'SupportsComplex',
            'SupportsFloat', 'SupportsInt', 'SupportsRound', 'TYPE_CHECKING',
            'Text', 'TextIO', 'Tuple', 'Type', 'TypeVar', 'Union',
            'ValuesView', 'cast', 'get_type_hints', 'no_type_check',
            'no_type_check_decorator', 'overload',
        )),
    ),
    (
        Version(3, 5, 7), frozenset((
            'AbstractSet', 'Any', 'AnyStr', 'AsyncContextManager',
            'AsyncIterable', 'AsyncIterator', 'Awaitable', 'BinaryIO',
            'ByteString', 'Callable', 'ChainMap', 'ClassVar', 'Container',
            'ContextManager', 'Coroutine', 'Counter', 'DefaultDict', 'Deque',
            'Dict', 'FrozenSet', 'Generator', 'Generic', 'GenericMeta',
            'Hashable', 'IO', 'ItemsView', 'Iterable', 'Iterator', 'KeysView',
            'List', 'Mapping', 'MappingView', 'Match', 'MutableMapping',
            'MutableSequence', 'MutableSet', 'NamedTuple', 'NewType',
            'NoReturn', 'Optional', 'Pattern', 'Reversible', 'Sequence', 'Set',
            'Sized', 'SupportsAbs', 'SupportsBytes', 'SupportsComplex',
            'SupportsFloat', 'SupportsInt', 'SupportsRound', 'TYPE_CHECKING',
            'Text', 'TextIO', 'Tuple', 'Type', 'TypeVar', 'Union',
            'ValuesView', 'cast', 'get_type_hints', 'no_type_check',
            'no_type_check_decorator', 'overload',
        )),
    ),
    (
        Version(3, 6, 0), frozenset((
            'AbstractSet', 'Any', 'AnyStr', 'AsyncIterable', 'AsyncIterator',
            'Awaitable', 'BinaryIO', 'ByteString', 'Callable', 'ClassVar',
            'Collection', 'Container', 'ContextManager', 'Coroutine',
            'DefaultDict', 'Dict', 'FrozenSet', 'Generator', 'Generic',
            'Hashable', 'IO', 'ItemsView', 'Iterable', 'Iterator', 'KeysView',
            'List', 'Mapping', 'MappingView', 'Match', 'MutableMapping',
            'MutableSequence', 'MutableSet', 'NamedTuple', 'NewType',
            'Optional', 'Pattern', 'Reversible', 'Sequence', 'Set', 'Sized',
            'SupportsAbs', 'SupportsBytes', 'SupportsComplex', 'SupportsFloat',
            'SupportsInt', 'SupportsRound', 'TYPE_CHECKING', 'Text', 'TextIO',
            'Tuple', 'Type', 'TypeVar', 'Union', 'ValuesView', 'cast',
            'get_type_hints', 'no_type_check', 'no_type_check_decorator',
            'overload',
        )),
    ),
    (
        Version(3, 6, 1), frozenset((
            'AbstractSet', 'Any', 'AnyStr', 'AsyncGenerator', 'AsyncIterable',
            'AsyncIterator', 'Awaitable', 'BinaryIO', 'ByteString', 'Callable',
            'ChainMap', 'ClassVar', 'Collection', 'Container',
            'ContextManager', 'Coroutine', 'Counter', 'DefaultDict', 'Deque',
            'Dict', 'FrozenSet', 'Generator', 'Generic', 'GenericMeta',
            'Hashable', 'IO', 'ItemsView', 'Iterable', 'Iterator', 'KeysView',
            'List', 'Mapping', 'MappingView', 'Match', 'MutableMapping',
            'MutableSequence', 'MutableSet', 'NamedTuple', 'NewType',
            'Optional', 'Pattern', 'Reversible', 'Sequence', 'Set', 'Sized',
            'SupportsAbs', 'SupportsBytes', 'SupportsComplex', 'SupportsFloat',
            'SupportsInt', 'SupportsRound', 'TYPE_CHECKING', 'Text', 'TextIO',
            'Tuple', 'Type', 'TypeVar', 'Union', 'ValuesView', 'cast',
            'get_type_hints', 'no_type_check', 'no_type_check_decorator',
            'overload',
        )),
    ),
    (
        Version(3, 6, 2), frozenset((
            'AbstractSet', 'Any', 'AnyStr', 'AsyncContextManager',
            'AsyncGenerator', 'AsyncIterable', 'AsyncIterator', 'Awaitable',
            'BinaryIO', 'ByteString', 'Callable', 'ChainMap', 'ClassVar',
            'Collection', 'Container', 'ContextManager', 'Coroutine',
            'Counter', 'DefaultDict', 'Deque', 'Dict', 'FrozenSet',
            'Generator', 'Generic', 'GenericMeta', 'Hashable', 'IO',
            'ItemsView', 'Iterable', 'Iterator', 'KeysView', 'List', 'Mapping',
            'MappingView', 'Match', 'MutableMapping', 'MutableSequence',
            'MutableSet', 'NamedTuple', 'NewType', 'NoReturn', 'Optional',
            'Pattern', 'Reversible', 'Sequence', 'Set', 'Sized', 'SupportsAbs',
            'SupportsBytes', 'SupportsComplex', 'SupportsFloat', 'SupportsInt',
            'SupportsRound', 'TYPE_CHECKING', 'Text', 'TextIO', 'Tuple',
            'Type', 'TypeVar', 'Union', 'ValuesView', 'cast', 'get_type_hints',
            'no_type_check', 'no_type_check_decorator', 'overload',
        )),
    ),
    (
        Version(3, 6, 3), frozenset((
            'AbstractSet', 'Any', 'AnyStr', 'AsyncContextManager',
            'AsyncGenerator', 'AsyncIterable', 'AsyncIterator', 'Awaitable',
            'BinaryIO', 'ByteString', 'Callable', 'ChainMap', 'ClassVar',
            'Collection', 'Container', 'ContextManager', 'Coroutine',
            'Counter', 'DefaultDict', 'Deque', 'Dict', 'FrozenSet',
            'Generator', 'Generic', 'GenericMeta', 'Hashable', 'IO',
            'ItemsView', 'Iterable', 'Iterator', 'KeysView', 'List', 'Mapping',
            'MappingView', 'Match', 'MutableMapping', 'MutableSequence',
            'MutableSet', 'NamedTuple', 'NewType', 'NoReturn', 'Optional',
            'Pattern', 'Reversible', 'Sequence', 'Set', 'Sized', 'SupportsAbs',
            'SupportsBytes', 'SupportsComplex', 'SupportsFloat', 'SupportsInt',
            'SupportsRound', 'TYPE_CHECKING', 'Text', 'TextIO', 'Tuple',
            'Type', 'TypeVar', 'Union', 'ValuesView', 'cast', 'get_type_hints',
            'no_type_check', 'no_type_check_decorator', 'overload',
        )),
    ),
    (
        Version(3, 6, 4), frozenset((
            'AbstractSet', 'Any', 'AnyStr', 'AsyncContextManager',
            'AsyncGenerator', 'AsyncIterable', 'AsyncIterator', 'Awaitable',
            'BinaryIO', 'ByteString', 'Callable', 'ChainMap', 'ClassVar',
            'Collection', 'Container', 'ContextManager', 'Coroutine',
            'Counter', 'DefaultDict', 'Deque', 'Dict', 'FrozenSet',
            'Generator', 'Generic', 'GenericMeta', 'Hashable', 'IO',
            'ItemsView', 'Iterable', 'Iterator', 'KeysView', 'List', 'Mapping',
            'MappingView', 'Match', 'MutableMapping', 'MutableSequence',
            'MutableSet', 'NamedTuple', 'NewType', 'NoReturn', 'Optional',
            'Pattern', 'Reversible', 'Sequence', 'Set', 'Sized', 'SupportsAbs',
            'SupportsBytes', 'SupportsComplex', 'SupportsFloat', 'SupportsInt',
            'SupportsRound', 'TYPE_CHECKING', 'Text', 'TextIO', 'Tuple',
            'Type', 'TypeVar', 'Union', 'ValuesView', 'cast', 'get_type_hints',
            'no_type_check', 'no_type_check_decorator', 'overload',
        )),
    ),
    (
        Version(3, 6, 5), frozenset((
            'AbstractSet', 'Any', 'AnyStr', 'AsyncContextManager',
            'AsyncGenerator', 'AsyncIterable', 'AsyncIterator', 'Awaitable',
            'BinaryIO', 'ByteString', 'Callable', 'ChainMap', 'ClassVar',
            'Collection', 'Container', 'ContextManager', 'Coroutine',
            'Counter', 'DefaultDict', 'Deque', 'Dict', 'FrozenSet',
            'Generator', 'Generic', 'GenericMeta', 'Hashable', 'IO',
            'ItemsView', 'Iterable', 'Iterator', 'KeysView', 'List', 'Mapping',
            'MappingView', 'Match', 'MutableMapping', 'MutableSequence',
            'MutableSet', 'NamedTuple', 'NewType', 'NoReturn', 'Optional',
            'Pattern', 'Reversible', 'Sequence', 'Set', 'Sized', 'SupportsAbs',
            'SupportsBytes', 'SupportsComplex', 'SupportsFloat', 'SupportsInt',
            'SupportsRound', 'TYPE_CHECKING', 'Text', 'TextIO', 'Tuple',
            'Type', 'TypeVar', 'Union', 'ValuesView', 'cast', 'get_type_hints',
            'no_type_check', 'no_type_check_decorator', 'overload',
        )),
    ),
    (
        Version(3, 6, 6), frozenset((
            'AbstractSet', 'Any', 'AnyStr', 'AsyncContextManager',
            'AsyncGenerator', 'AsyncIterable', 'AsyncIterator', 'Awaitable',
            'BinaryIO', 'ByteString', 'Callable', 'ChainMap', 'ClassVar',
            'Collection', 'Container', 'ContextManager', 'Coroutine',
            'Counter', 'DefaultDict', 'Deque', 'Dict', 'FrozenSet',
            'Generator', 'Generic', 'GenericMeta', 'Hashable', 'IO',
            'ItemsView', 'Iterable', 'Iterator', 'KeysView', 'List', 'Mapping',
            'MappingView', 'Match', 'MutableMapping', 'MutableSequence',
            'MutableSet', 'NamedTuple', 'NewType', 'NoReturn', 'Optional',
            'Pattern', 'Reversible', 'Sequence', 'Set', 'Sized', 'SupportsAbs',
            'SupportsBytes', 'SupportsComplex', 'SupportsFloat', 'SupportsInt',
            'SupportsRound', 'TYPE_CHECKING', 'Text', 'TextIO', 'Tuple',
            'Type', 'TypeVar', 'Union', 'ValuesView', 'cast', 'get_type_hints',
            'no_type_check', 'no_type_check_decorator', 'overload',
        )),
    ),
    (
        Version(3, 6, 7), frozenset((
            'AbstractSet', 'Any', 'AnyStr', 'AsyncContextManager',
            'AsyncGenerator', 'AsyncIterable', 'AsyncIterator', 'Awaitable',
            'BinaryIO', 'ByteString', 'Callable', 'ChainMap', 'ClassVar',
            'Collection', 'Container', 'ContextManager', 'Coroutine',
            'Counter', 'DefaultDict', 'Deque', 'Dict', 'FrozenSet',
            'Generator', 'Generic', 'GenericMeta', 'Hashable', 'IO',
            'ItemsView', 'Iterable', 'Iterator', 'KeysView', 'List', 'Mapping',
            'MappingView', 'Match', 'MutableMapping', 'MutableSequence',
            'MutableSet', 'NamedTuple', 'NewType', 'NoReturn', 'Optional',
            'Pattern', 'Reversible', 'Sequence', 'Set', 'Sized', 'SupportsAbs',
            'SupportsBytes', 'SupportsComplex', 'SupportsFloat', 'SupportsInt',
            'SupportsRound', 'TYPE_CHECKING', 'Text', 'TextIO', 'Tuple',
            'Type', 'TypeVar', 'Union', 'ValuesView', 'cast', 'get_type_hints',
            'no_type_check', 'no_type_check_decorator', 'overload',
        )),
    ),
    (
        Version(3, 6, 8), frozenset((
            'AbstractSet', 'Any', 'AnyStr', 'AsyncContextManager',
            'AsyncGenerator', 'AsyncIterable', 'AsyncIterator', 'Awaitable',
            'BinaryIO', 'ByteString', 'Callable', 'ChainMap', 'ClassVar',
            'Collection', 'Container', 'ContextManager', 'Coroutine',
            'Counter', 'DefaultDict', 'Deque', 'Dict', 'FrozenSet',
            'Generator', 'Generic', 'GenericMeta', 'Hashable', 'IO',
            'ItemsView', 'Iterable', 'Iterator', 'KeysView', 'List', 'Mapping',
            'MappingView', 'Match', 'MutableMapping', 'MutableSequence',
            'MutableSet', 'NamedTuple', 'NewType', 'NoReturn', 'Optional',
            'Pattern', 'Reversible', 'Sequence', 'Set', 'Sized', 'SupportsAbs',
            'SupportsBytes', 'SupportsComplex', 'SupportsFloat', 'SupportsInt',
            'SupportsRound', 'TYPE_CHECKING', 'Text', 'TextIO', 'Tuple',
            'Type', 'TypeVar', 'Union', 'ValuesView', 'cast', 'get_type_hints',
            'no_type_check', 'no_type_check_decorator', 'overload',
        )),
    ),
    (
        Version(3, 6, 9), frozenset((
            'AbstractSet', 'Any', 'AnyStr', 'AsyncContextManager',
            'AsyncGenerator', 'AsyncIterable', 'AsyncIterator', 'Awaitable',
            'BinaryIO', 'ByteString', 'Callable', 'ChainMap', 'ClassVar',
            'Collection', 'Container', 'ContextManager', 'Coroutine',
            'Counter', 'DefaultDict', 'Deque', 'Dict', 'FrozenSet',
            'Generator', 'Generic', 'GenericMeta', 'Hashable', 'IO',
            'ItemsView', 'Iterable', 'Iterator', 'KeysView', 'List', 'Mapping',
            'MappingView', 'Match', 'MutableMapping', 'MutableSequence',
            'MutableSet', 'NamedTuple', 'NewType', 'NoReturn', 'Optional',
            'Pattern', 'Reversible', 'Sequence', 'Set', 'Sized', 'SupportsAbs',
            'SupportsBytes', 'SupportsComplex', 'SupportsFloat', 'SupportsInt',
            'SupportsRound', 'TYPE_CHECKING', 'Text', 'TextIO', 'Tuple',
            'Type', 'TypeVar', 'Union', 'ValuesView', 'cast', 'get_type_hints',
            'no_type_check', 'no_type_check_decorator', 'overload',
        )),
    ),
    (
        Version(3, 7, 0), frozenset((
            'AbstractSet', 'Any', 'AnyStr', 'AsyncContextManager',
            'AsyncGenerator', 'AsyncIterable', 'AsyncIterator', 'Awaitable',
            'BinaryIO', 'ByteString', 'Callable', 'ChainMap', 'ClassVar',
            'Collection', 'Container', 'ContextManager', 'Coroutine',
            'Counter', 'DefaultDict', 'Deque', 'Dict', 'ForwardRef',
            'FrozenSet', 'Generator', 'Generic', 'Hashable', 'IO', 'ItemsView',
            'Iterable', 'Iterator', 'KeysView', 'List', 'Mapping',
            'MappingView', 'Match', 'MutableMapping', 'MutableSequence',
            'MutableSet', 'NamedTuple', 'NewType', 'NoReturn', 'Optional',
            'Pattern', 'Reversible', 'Sequence', 'Set', 'Sized', 'SupportsAbs',
            'SupportsBytes', 'SupportsComplex', 'SupportsFloat', 'SupportsInt',
            'SupportsRound', 'TYPE_CHECKING', 'Text', 'TextIO', 'Tuple',
            'Type', 'TypeVar', 'Union', 'ValuesView', 'cast', 'get_type_hints',
            'no_type_check', 'no_type_check_decorator', 'overload',
        )),
    ),
    (
        Version(3, 7, 1), frozenset((
            'AbstractSet', 'Any', 'AnyStr', 'AsyncContextManager',
            'AsyncGenerator', 'AsyncIterable', 'AsyncIterator', 'Awaitable',
            'BinaryIO', 'ByteString', 'Callable', 'ChainMap', 'ClassVar',
            'Collection', 'Container', 'ContextManager', 'Coroutine',
            'Counter', 'DefaultDict', 'Deque', 'Dict', 'ForwardRef',
            'FrozenSet', 'Generator', 'Generic', 'Hashable', 'IO', 'ItemsView',
            'Iterable', 'Iterator', 'KeysView', 'List', 'Mapping',
            'MappingView', 'Match', 'MutableMapping', 'MutableSequence',
            'MutableSet', 'NamedTuple', 'NewType', 'NoReturn', 'Optional',
            'Pattern', 'Reversible', 'Sequence', 'Set', 'Sized', 'SupportsAbs',
            'SupportsBytes', 'SupportsComplex', 'SupportsFloat', 'SupportsInt',
            'SupportsRound', 'TYPE_CHECKING', 'Text', 'TextIO', 'Tuple',
            'Type', 'TypeVar', 'Union', 'ValuesView', 'cast', 'get_type_hints',
            'no_type_check', 'no_type_check_decorator', 'overload',
        )),
    ),
    (
        Version(3, 7, 2), frozenset((
            'AbstractSet', 'Any', 'AnyStr', 'AsyncContextManager',
            'AsyncGenerator', 'AsyncIterable', 'AsyncIterator', 'Awaitable',
            'BinaryIO', 'ByteString', 'Callable', 'ChainMap', 'ClassVar',
            'Collection', 'Container', 'ContextManager', 'Coroutine',
            'Counter', 'DefaultDict', 'Deque', 'Dict', 'ForwardRef',
            'FrozenSet', 'Generator', 'Generic', 'Hashable', 'IO', 'ItemsView',
            'Iterable', 'Iterator', 'KeysView', 'List', 'Mapping',
            'MappingView', 'Match', 'MutableMapping', 'MutableSequence',
            'MutableSet', 'NamedTuple', 'NewType', 'NoReturn', 'Optional',
            'OrderedDict', 'Pattern', 'Reversible', 'Sequence', 'Set', 'Sized',
            'SupportsAbs', 'SupportsBytes', 'SupportsComplex', 'SupportsFloat',
            'SupportsInt', 'SupportsRound', 'TYPE_CHECKING', 'Text', 'TextIO',
            'Tuple', 'Type', 'TypeVar', 'Union', 'ValuesView', 'cast',
            'get_type_hints', 'no_type_check', 'no_type_check_decorator',
            'overload',
        )),
    ),
    (
        Version(3, 7, 3), frozenset((
            'AbstractSet', 'Any', 'AnyStr', 'AsyncContextManager',
            'AsyncGenerator', 'AsyncIterable', 'AsyncIterator', 'Awaitable',
            'BinaryIO', 'ByteString', 'Callable', 'ChainMap', 'ClassVar',
            'Collection', 'Container', 'ContextManager', 'Coroutine',
            'Counter', 'DefaultDict', 'Deque', 'Dict', 'ForwardRef',
            'FrozenSet', 'Generator', 'Generic', 'Hashable', 'IO', 'ItemsView',
            'Iterable', 'Iterator', 'KeysView', 'List', 'Mapping',
            'MappingView', 'Match', 'MutableMapping', 'MutableSequence',
            'MutableSet', 'NamedTuple', 'NewType', 'NoReturn', 'Optional',
            'OrderedDict', 'Pattern', 'Reversible', 'Sequence', 'Set', 'Sized',
            'SupportsAbs', 'SupportsBytes', 'SupportsComplex', 'SupportsFloat',
            'SupportsInt', 'SupportsRound', 'TYPE_CHECKING', 'Text', 'TextIO',
            'Tuple', 'Type', 'TypeVar', 'Union', 'ValuesView', 'cast',
            'get_type_hints', 'no_type_check', 'no_type_check_decorator',
            'overload',
        )),
    ),
    (
        Version(3, 7, 4), frozenset((
            'AbstractSet', 'Any', 'AnyStr', 'AsyncContextManager',
            'AsyncGenerator', 'AsyncIterable', 'AsyncIterator', 'Awaitable',
            'BinaryIO', 'ByteString', 'Callable', 'ChainMap', 'ClassVar',
            'Collection', 'Container', 'ContextManager', 'Coroutine',
            'Counter', 'DefaultDict', 'Deque', 'Dict', 'ForwardRef',
            'FrozenSet', 'Generator', 'Generic', 'Hashable', 'IO', 'ItemsView',
            'Iterable', 'Iterator', 'KeysView', 'List', 'Mapping',
            'MappingView', 'Match', 'MutableMapping', 'MutableSequence',
            'MutableSet', 'NamedTuple', 'NewType', 'NoReturn', 'Optional',
            'OrderedDict', 'Pattern', 'Reversible', 'Sequence', 'Set', 'Sized',
            'SupportsAbs', 'SupportsBytes', 'SupportsComplex', 'SupportsFloat',
            'SupportsInt', 'SupportsRound', 'TYPE_CHECKING', 'Text', 'TextIO',
            'Tuple', 'Type', 'TypeVar', 'Union', 'ValuesView', 'cast',
            'get_type_hints', 'no_type_check', 'no_type_check_decorator',
            'overload',
        )),
    ),
)
# END GENERATED
VERSIONS = frozenset(version for version, _ in SYMBOLS)


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self._level = -1
        self.imports: Dict[str, List[Tuple[int, int]]]
        self.imports = collections.defaultdict(list)
        self.attributes: Dict[str, List[Tuple[int, int]]]
        self.attributes = collections.defaultdict(list)
        self.defined_overload = False
        self.unions_pattern_or_match: List[Tuple[int, int]] = []
        self.from_imported_names: Set[str] = set()
        self._in_namedtuple = False
        self.namedtuple_methods: List[Tuple[int, int]] = []
        self.namedtuple_defaults: List[Tuple[int, int]] = []

    def _is_typing(self, node: ast.AST, names: Tuple[str, ...]) -> bool:
        return (
            isinstance(node, ast.Name) and
            node.id in names and
            node.id in self.from_imported_names
        ) or (
            isinstance(node, ast.Attribute) and
            isinstance(node.value, ast.Name) and
            node.value.id == 'typing' and
            node.attr in names
        )

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        if node.level == 0 and node.module == 'typing' and self._level == 0:
            for name in node.names:
                self.imports[name.name].append((node.lineno, node.col_offset))
                if not name.asname:
                    self.from_imported_names.add(name.name)

        self.generic_visit(node)

    def visit_Attribute(self, node: ast.Attribute) -> None:
        if (
                isinstance(node, ast.Attribute) and
                isinstance(node.value, ast.Name) and
                node.value.id == 'typing'
        ):
            self.attributes[node.attr].append((node.lineno, node.col_offset))

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        if self._level == 1 and node.name == 'overload':
            self.defined_overload = True
        if self._in_namedtuple:
            self.namedtuple_methods.append((node.lineno, node.col_offset))
        self.generic_visit(node)

    def visit_Subscript(self, node: ast.Subscript) -> None:
        if (
            self._is_typing(node.value, ('Union',)) and
            isinstance(node.slice, ast.Index) and
            isinstance(node.slice.value, ast.Tuple) and
            len(node.slice.value.elts) > 1 and
            any(
                self._is_typing(x, ('Pattern', 'Match'))
                for x in node.slice.value.elts
            )
        ):
            self.unions_pattern_or_match.append((node.lineno, node.col_offset))
        self.generic_visit(node)

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        if any(self._is_typing(base, ('NamedTuple',)) for base in node.bases):
            self._in_namedtuple = True
            try:
                self.generic_visit(node)
            finally:
                self._in_namedtuple = False
        else:
            self.generic_visit(node)

    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
        if self._in_namedtuple and node.value is not None:
            self.namedtuple_defaults.append((node.lineno, node.col_offset))
        self.generic_visit(node)

    def generic_visit(self, node: ast.AST) -> None:
        self._level += 1
        super().generic_visit(node)
        self._level -= 1


class Plugin:
    name = __name__
    version = importlib_metadata.version(__name__)

    _min_python_version = Version(3, 5, 0)

    @staticmethod
    def add_options(option_manager: Any) -> None:
        option_manager.add_option(
            '--min-python-version', type='str', metavar='VERSION',
            default='3.5.0', parse_from_config=True,
            help=(
                'Minimum version of python your code supports, '
                '(default: %(default)s)'
            ),
        )

    @classmethod
    def parse_options(cls, options: Any) -> None:
        cfg = configparser.ConfigParser()
        cfg.add_section('options')
        cfg['options']['python_requires'] = f'>={options.min_python_version}'

        if os.path.exists('setup.cfg'):
            cfg.read('setup.cfg')

        v = cls._min_python_version
        for part in cfg['options']['python_requires'].split(','):
            part = part.strip()
            if part.startswith('>='):
                v = Version.parse(part[2:])

        v = max(v, SYMBOLS[0][0])
        if v not in VERSIONS:
            raise ValueError(f'min-python-version ({v}): unknown version')
        cls._min_python_version = v

    def __init__(self, tree: ast.AST):
        self._tree = tree

    def _version_specific_errors(
            self,
            msg: str,
            name_positions: Dict[str, List[Tuple[int, int]]],
    ) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        error_versions: Dict[Tuple[int, int, str], List[Version]]
        error_versions = collections.defaultdict(list)

        for version, symbols in SYMBOLS:
            if version < self._min_python_version:
                continue
            for k in set(name_positions) - symbols:
                for line, col in name_positions[k]:
                    error_versions[(line, col, k)].append(version)

        for (line, col, k), versions in error_versions.items():
            versions_s = ', '.join(str(v) for v in versions)
            yield line, col, msg.format(k, versions_s), type(self)

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)

        if self._min_python_version < Version(3, 5, 2):
            guard = '`if False:  # TYPE_CHECKING`'
        else:
            guard = '`if TYPE_CHECKING:`'
        msg = f'TYP001 guard import by {guard}: {{}} (not in {{}})'
        yield from self._version_specific_errors(msg, visitor.imports)

        msg = (
            'TYP002 @overload is broken in <3.5.2, '
            'add `if sys.version_info < (3, 5, 2): def overload(f): return f`'
        )
        if (
                self._min_python_version < Version(3, 5, 2) and
                'overload' in visitor.imports and
                not visitor.defined_overload
        ):
            for line, col in visitor.imports['overload']:
                yield line, col, msg, type(self)

        msg = (
            'TYP003 Union[Match, ...] or Union[Pattern, ...] '
            'must be quoted in <3.5.2'
        )
        if (
                self._min_python_version < Version(3, 5, 2) and
                visitor.unions_pattern_or_match
        ):
            for line, col in visitor.unions_pattern_or_match:
                yield line, col, msg, type(self)

        msg = 'TYP004 NamedTuple does not support methods in 3.6.0'
        if (
                self._min_python_version < Version(3, 6, 1) and
                visitor.namedtuple_methods
        ):
            for line, col in visitor.namedtuple_methods:
                yield line, col, msg, type(self)

        msg = 'TYP005 NamedTuple does not support defaults in 3.6.0'
        if (
                self._min_python_version < Version(3, 6, 1) and
                visitor.namedtuple_defaults
        ):
            for line, col in visitor.namedtuple_defaults:
                yield line, col, msg, type(self)

        msg = 'TYP006 guard `typing` attribute by quoting: {} (not in {})'
        yield from self._version_specific_errors(msg, visitor.attributes)
