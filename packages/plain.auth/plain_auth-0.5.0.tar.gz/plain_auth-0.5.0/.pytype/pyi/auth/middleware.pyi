# (generated with --quick)

from plain import auth
from typing import Any

ImproperlyConfigured: Any
SimpleLazyObject: Any

class AuthenticationMiddleware:
    def __call__(self, request) -> Any: ...
    def __init__(self, get_response) -> None: ...
    def get_response(self, _1) -> Any: ...

def get_user(request) -> Any: ...
