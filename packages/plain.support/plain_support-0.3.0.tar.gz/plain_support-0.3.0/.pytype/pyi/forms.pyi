# (generated with --quick)

from typing import Any

ModelForm: Any
SupportFormEntry: Any
TemplateEmail: Any
get_user_model: Any
settings: Any

class SupportForm(Any):
    class Meta:
        fields: list[str]
        model: Any
    __doc__: str
    form_slug: Any
    user: Any
    def __init__(self, user, form_slug, *args, **kwargs) -> None: ...
    def find_user(self) -> Any: ...
    def notify(self, instance) -> None: ...
    def save(self, commit = ...) -> Any: ...
