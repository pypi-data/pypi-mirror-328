# (generated with --quick)

import time
import zlib
from typing import Any

JSONSerializer: Any
SignatureExpired: Any
Signer: Any
b62_decode: Any
b62_encode: Any
b64_decode: Any
b64_encode: Any

class ExpiringSigner(Any):
    __doc__: str
    def sign(self, value, expires_in) -> Any: ...
    def sign_object(self, obj, serializer = ..., compress = ..., expires_in = ...) -> Any: ...
    def unsign(self, value) -> Any: ...
    def unsign_object(self, signed_obj, serializer = ...) -> Any: ...

def dumps(obj, key = ..., salt = ..., serializer = ..., compress = ..., expires_in = ...) -> Any: ...
def loads(s, key = ..., salt = ..., serializer = ..., fallback_keys = ...) -> Any: ...
