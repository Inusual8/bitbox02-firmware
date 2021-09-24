# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class PubResponse(google___protobuf___message___Message):
    pub = ... # type: typing___Text

    def __init__(self,
        *,
        pub : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PubResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"pub"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"pub",b"pub"]) -> None: ...

class RootFingerprintRequest(google___protobuf___message___Message):

    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> RootFingerprintRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class RootFingerprintResponse(google___protobuf___message___Message):
    fingerprint = ... # type: bytes

    def __init__(self,
        *,
        fingerprint : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> RootFingerprintResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"fingerprint"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"fingerprint",b"fingerprint"]) -> None: ...

class XPub(google___protobuf___message___Message):
    depth = ... # type: bytes
    parent_fingerprint = ... # type: bytes
    child_num = ... # type: int
    chain_code = ... # type: bytes
    public_key = ... # type: bytes

    def __init__(self,
        *,
        depth : typing___Optional[bytes] = None,
        parent_fingerprint : typing___Optional[bytes] = None,
        child_num : typing___Optional[int] = None,
        chain_code : typing___Optional[bytes] = None,
        public_key : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> XPub: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"chain_code",u"child_num",u"depth",u"parent_fingerprint",u"public_key"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"chain_code",b"chain_code",u"child_num",b"child_num",u"depth",b"depth",u"parent_fingerprint",b"parent_fingerprint",u"public_key",b"public_key"]) -> None: ...

class Keypath(google___protobuf___message___Message):
    keypath = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[int]

    def __init__(self,
        *,
        keypath : typing___Optional[typing___Iterable[int]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Keypath: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"keypath"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"keypath",b"keypath"]) -> None: ...
