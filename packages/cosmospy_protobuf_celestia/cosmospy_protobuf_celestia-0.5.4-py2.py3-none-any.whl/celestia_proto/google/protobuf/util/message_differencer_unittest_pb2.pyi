from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestField(_message.Message):
    __slots__ = ("a", "b", "c", "rc", "m", "rm")
    TF_FIELD_NUMBER: _ClassVar[int]
    tf: _descriptor.FieldDescriptor
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    C_FIELD_NUMBER: _ClassVar[int]
    RC_FIELD_NUMBER: _ClassVar[int]
    M_FIELD_NUMBER: _ClassVar[int]
    RM_FIELD_NUMBER: _ClassVar[int]
    a: int
    b: int
    c: int
    rc: _containers.RepeatedScalarFieldContainer[int]
    m: TestField
    rm: _containers.RepeatedCompositeFieldContainer[TestField]
    def __init__(self, a: _Optional[int] = ..., b: _Optional[int] = ..., c: _Optional[int] = ..., rc: _Optional[_Iterable[int]] = ..., m: _Optional[_Union[TestField, _Mapping]] = ..., rm: _Optional[_Iterable[_Union[TestField, _Mapping]]] = ...) -> None: ...

class TestDiffMessage(_message.Message):
    __slots__ = ("item", "v", "w", "m", "rv", "rw", "rm", "rany")
    Extensions: _python_message._ExtensionDict
    class Item(_message.Message):
        __slots__ = ("a", "b", "ra", "rb", "m", "rm", "mp")
        class MpEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: int
            def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
        A_FIELD_NUMBER: _ClassVar[int]
        B_FIELD_NUMBER: _ClassVar[int]
        RA_FIELD_NUMBER: _ClassVar[int]
        RB_FIELD_NUMBER: _ClassVar[int]
        M_FIELD_NUMBER: _ClassVar[int]
        RM_FIELD_NUMBER: _ClassVar[int]
        MP_FIELD_NUMBER: _ClassVar[int]
        a: int
        b: str
        ra: _containers.RepeatedScalarFieldContainer[int]
        rb: _containers.RepeatedScalarFieldContainer[str]
        m: TestField
        rm: _containers.RepeatedCompositeFieldContainer[TestField]
        mp: _containers.ScalarMap[str, int]
        def __init__(self, a: _Optional[int] = ..., b: _Optional[str] = ..., ra: _Optional[_Iterable[int]] = ..., rb: _Optional[_Iterable[str]] = ..., m: _Optional[_Union[TestField, _Mapping]] = ..., rm: _Optional[_Iterable[_Union[TestField, _Mapping]]] = ..., mp: _Optional[_Mapping[str, int]] = ...) -> None: ...
    ITEM_FIELD_NUMBER: _ClassVar[int]
    V_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    M_FIELD_NUMBER: _ClassVar[int]
    RV_FIELD_NUMBER: _ClassVar[int]
    RW_FIELD_NUMBER: _ClassVar[int]
    RM_FIELD_NUMBER: _ClassVar[int]
    RANY_FIELD_NUMBER: _ClassVar[int]
    item: _containers.RepeatedCompositeFieldContainer[TestDiffMessage.Item]
    v: int
    w: str
    m: TestField
    rv: _containers.RepeatedScalarFieldContainer[int]
    rw: _containers.RepeatedScalarFieldContainer[str]
    rm: _containers.RepeatedCompositeFieldContainer[TestField]
    rany: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, item: _Optional[_Iterable[_Union[TestDiffMessage.Item, _Mapping]]] = ..., v: _Optional[int] = ..., w: _Optional[str] = ..., m: _Optional[_Union[TestField, _Mapping]] = ..., rv: _Optional[_Iterable[int]] = ..., rw: _Optional[_Iterable[str]] = ..., rm: _Optional[_Iterable[_Union[TestField, _Mapping]]] = ..., rany: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...
