# (generated with --quick)

from plain import models
from typing import Any

class Session(Any):
    __doc__: str
    expire_date: Any
    objects: SessionManager
    session_data: Any
    session_key: Any
    def __str__(self) -> Any: ...
    def get_decoded(self) -> Any: ...
    @classmethod
    def get_session_store_class(cls) -> Any: ...

class SessionManager(Any):
    use_in_migrations: bool
    def encode(self, session_dict) -> Any: ...
    def save(self, session_key, session_dict, expire_date) -> Any: ...
