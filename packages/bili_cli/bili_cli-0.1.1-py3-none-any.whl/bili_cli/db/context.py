#  from typing import (
#  Dict
#  )
from contextvars import ContextVar
from sqlalchemy.orm import sessionmaker

__all__ = ['open_session', 'get_session']


class SessionWebContent:
    database_uri: str = None
    session: sessionmaker = None


session_web_context: ContextVar[SessionWebContent] = ContextVar(
    'session_web_context', default=SessionWebContent())


class Session:
    _session: sessionmaker
    _sessionmaker: type

    def __init__(self, _sessionmaker: type):
        self._sessionmaker = _sessionmaker
        self._session = self._sessionmaker()

    def __enter__(self) -> sessionmaker:
        return self._session

    def __exit__(self, ext_type, ext_val, ext_tb):
        self._session.close()


def open_session(sessionmaker: type) -> sessionmaker:
    _session = Session(sessionmaker)
    session_web_context.get().session = _session.__enter__()
    return _session


def get_session() -> sessionmaker:
    return session_web_context.get().session
