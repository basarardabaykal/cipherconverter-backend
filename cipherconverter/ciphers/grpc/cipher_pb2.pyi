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

class CipherResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bytes
    def __init__(self, result: _Optional[bytes] = ...) -> None: ...
