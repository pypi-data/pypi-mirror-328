# (generated with --quick)

from loginlink import signing
from typing import Any

BadSignature: Any
SignatureExpired: Any
get_user_model: Any
reverse: Any

class LoginLinkChanged(Exception): ...

class LoginLinkExpired(Exception): ...

class LoginLinkInvalid(Exception): ...

def generate_link_url(*, request, user, email, expires_in) -> Any: ...
def get_link_token_user(token) -> Any: ...
