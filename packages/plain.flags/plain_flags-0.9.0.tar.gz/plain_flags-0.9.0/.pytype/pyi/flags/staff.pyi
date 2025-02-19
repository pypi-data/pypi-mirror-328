# (generated with --quick)

import functools
from typing import Annotated, Any

Card: Any
Flag: Any
FlagResult: Any
FlagResultStaff: Any
FlagStaff: Any
ModelForm: Any
StaffModelDetailView: Any
StaffModelListView: Any
StaffModelUpdateView: Any
StaffModelViewset: Any
cached_property: type[functools.cached_property]
register_viewset: Any

class FlagResultForm(Any):
    class Meta:
        fields: list[str]
        model: Any

class UnusedFlagsCard(Any):
    flag_errors: Annotated[Any, 'property']
    title: str
    def get_number(self) -> int: ...
    def get_text(self) -> str: ...
