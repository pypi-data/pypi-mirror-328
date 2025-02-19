# (generated with --quick)

from plain import forms
from typing import Any

ModelForm: Any
ValidationError: Any
get_user_model: Any

class PasswordLoginForm(Any):
    _user: Any
    email: Any
    password: Any
    def clean(self) -> Any: ...
    def get_user(self) -> Any: ...

class PasswordSignupForm(Any):
    class Meta:
        fields: tuple[str, str]
        model: Any
    confirm_password: Any
    def clean(self) -> Any: ...

def check_password(password, encoded, setter = ..., preferred = ...) -> Any: ...
def check_user_password(user, password) -> Any: ...
