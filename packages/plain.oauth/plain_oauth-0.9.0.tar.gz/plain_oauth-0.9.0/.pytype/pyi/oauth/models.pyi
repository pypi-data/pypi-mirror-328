# (generated with --quick)

import oauth.exceptions
import oauth.providers
from plain import models
from plain.models import transaction
from plain.utils import timezone
from typing import Any, TypeVar

Error: Any
IntegrityError: Any
OAuthToken: type[oauth.providers.OAuthToken]
OAuthUser: type[oauth.providers.OAuthUser]
OAuthUserAlreadyExistsError: type[oauth.exceptions.OAuthUserAlreadyExistsError]
OperationalError: Any
ProgrammingError: Any
ValidationError: Any
get_user_model: Any
settings: Any

_TOAuthConnection = TypeVar('_TOAuthConnection', bound=OAuthConnection)

class OAuthConnection(Any):
    class Meta:
        constraints: list
        ordering: tuple[str]
    access_token: Any
    access_token_expires_at: Any
    created_at: Any
    provider_key: Any
    provider_user_id: Any
    refresh_token: Any
    refresh_token_expires_at: Any
    updated_at: Any
    user: Any
    def __str__(self) -> str: ...
    def access_token_expired(self) -> bool: ...
    @classmethod
    def check(cls, **kwargs) -> Any: ...
    @classmethod
    def connect(cls: type[_TOAuthConnection], *, user, provider_key: str, oauth_token: oauth.providers.OAuthToken, oauth_user: oauth.providers.OAuthUser) -> _TOAuthConnection: ...
    @classmethod
    def get_or_create_user(cls: type[_TOAuthConnection], *, provider_key: str, oauth_token: oauth.providers.OAuthToken, oauth_user: oauth.providers.OAuthUser) -> _TOAuthConnection: ...
    def refresh_access_token(self) -> None: ...
    def refresh_token_expired(self) -> bool: ...
    def set_token_fields(self, oauth_token: oauth.providers.OAuthToken) -> None: ...
    def set_user_fields(self, oauth_user: oauth.providers.OAuthUser) -> None: ...
