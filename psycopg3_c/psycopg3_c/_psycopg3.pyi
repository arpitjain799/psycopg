"""
Stub representaton of the public objects exposed by the _psycopg3 module.

TODO: this should be generated by mypy's stubgen but it crashes with no
information. Will submit a bug.
"""

# Copyright (C) 2020 The Psycopg Team

from typing import Any, Iterable, List, Optional, Sequence, Tuple

from psycopg3.adapt import Dumper, Loader, AdaptersMap
from psycopg3.proto import AdaptContext, PQGen, PQGenConn
from psycopg3.connection import BaseConnection
from psycopg3.pq import Format
from psycopg3.pq.proto import PGconn, PGresult

class Transformer(AdaptContext):
    def __init__(self, context: Optional[AdaptContext] = None): ...
    @property
    def connection(self) -> Optional[BaseConnection]: ...
    @property
    def adapters(self) -> AdaptersMap: ...
    @property
    def pgresult(self) -> Optional[PGresult]: ...
    @pgresult.setter
    def pgresult(self, result: Optional[PGresult]) -> None: ...
    def set_row_types(
        self, types: Sequence[int], formats: Sequence[Format]
    ) -> None: ...
    def get_dumper(self, obj: Any, format: Format) -> Dumper: ...
    def load_row(self, row: int) -> Optional[Tuple[Any, ...]]: ...
    def load_sequence(
        self, record: Sequence[Optional[bytes]]
    ) -> Tuple[Any, ...]: ...
    def get_loader(self, oid: int, format: Format) -> Loader: ...

def register_builtin_c_adapters() -> None: ...
def connect(conninfo: str) -> PQGenConn[PGconn]: ...
def execute(pgconn: PGconn) -> PQGen[List[PGresult]]: ...

# vim: set syntax=python:
