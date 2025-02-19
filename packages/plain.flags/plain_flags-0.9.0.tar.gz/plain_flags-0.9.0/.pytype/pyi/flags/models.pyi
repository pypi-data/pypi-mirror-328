# (generated with --quick)

import flags.exceptions
import flags.flags
import re
import uuid
from plain import models
from typing import Any

FlagImportError: type[flags.exceptions.FlagImportError]
Info: Any
ProgrammingError: Any
ValidationError: Any
settings: Any

class Flag(Any):
    created_at: Any
    description: Any
    enabled: Any
    name: Any
    updated_at: Any
    used_at: Any
    uuid: Any
    def __str__(self) -> Any: ...
    @classmethod
    def check(cls, **kwargs) -> Any: ...

class FlagResult(Any):
    class Meta:
        constraints: list
    created_at: Any
    flag: Any
    key: Any
    updated_at: Any
    uuid: Any
    value: Any
    def __str__(self) -> Any: ...

def get_flag_class(flag_name: str) -> flags.flags.Flag: ...
def validate_flag_name(value) -> None: ...
