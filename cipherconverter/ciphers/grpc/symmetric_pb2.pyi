import common_pb2 as _common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CaesarRequest(_message.Message):
    __slots__ = ("text", "shift")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SHIFT_FIELD_NUMBER: _ClassVar[int]
    text: bytes
    shift: int
    def __init__(self, text: _Optional[bytes] = ..., shift: _Optional[int] = ...) -> None: ...

class ColumnarRequest(_message.Message):
    __slots__ = ("text", "columns")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    text: bytes
    columns: int
    def __init__(self, text: _Optional[bytes] = ..., columns: _Optional[int] = ...) -> None: ...

class OTPRequest(_message.Message):
    __slots__ = ("text", "key")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    text: bytes
    key: bytes
    def __init__(self, text: _Optional[bytes] = ..., key: _Optional[bytes] = ...) -> None: ...

class AffineRequest(_message.Message):
    __slots__ = ("text", "a", "b")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    text: bytes
    a: int
    b: int
    def __init__(self, text: _Optional[bytes] = ..., a: _Optional[int] = ..., b: _Optional[int] = ...) -> None: ...
