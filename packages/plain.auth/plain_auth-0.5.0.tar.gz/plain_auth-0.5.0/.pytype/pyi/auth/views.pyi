# (generated with --quick)

import urllib.parse
from typing import Any, Iterable, Literal, Optional, TypeVar, Union, overload

Http404: Any
PermissionDenied: Any
QueryDict: Any
Response: Any
ResponseRedirect: Any
View: Any
reverse: Any
settings: Any

AnyStr = TypeVar('AnyStr', str, bytes)

class AuthViewMixin:
    login_required: bool
    login_url: None
    staff_required: bool
    def check_auth(self) -> None: ...
    def get_response(self) -> Any: ...

class LoginRequired(Exception):
    login_url: Any
    redirect_field_name: Any
    def __init__(self, login_url = ..., redirect_field_name = ...) -> None: ...

class LogoutView(Any):
    def post(self) -> Any: ...

def logout(request) -> None: ...
def redirect_to_login(next, login_url = ..., redirect_field_name = ...) -> Any: ...
def resolve_url(to, *args, **kwargs) -> Any: ...
@overload
def urlparse(url: str, scheme: str = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResult: ...
@overload
def urlparse(url: Optional[bytes], scheme: Optional[Union[bytes, Literal['']]] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResultBytes: ...
@overload
def urlunparse(components: Iterable[None]) -> Literal[b'']: ...
@overload
def urlunparse(components: Iterable[Optional[AnyStr]]) -> AnyStr: ...
