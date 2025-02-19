# (generated with --quick)

import mail.message
import mail.utils
from typing import Any, Optional, TypeVar

BadHeaderError: type[mail.message.BadHeaderError]
CachedDnsName: type[mail.utils.CachedDnsName]
DEFAULT_ATTACHMENT_MIME_TYPE: str
DNS_NAME: mail.utils.CachedDnsName
EmailMessage: type[mail.message.EmailMessage]
EmailMultiAlternatives: type[mail.message.EmailMultiAlternatives]
SafeMIMEMultipart: type[mail.message.SafeMIMEMultipart]
SafeMIMEText: type[mail.message.SafeMIMEText]
TemplateEmail: type[mail.message.TemplateEmail]
__all__: list[str]
import_string: Any
settings: Any

_T0 = TypeVar('_T0')

def forbid_multi_line_headers(name: _T0, val, encoding) -> tuple[_T0, str]: ...
def get_connection(backend = ..., fail_silently = ..., **kwds) -> Any: ...
def make_msgid(idstring: Optional[str] = ..., domain: Optional[str] = ...) -> str: ...
def send_mail(subject, message, from_email, recipient_list, fail_silently = ..., auth_user = ..., auth_password = ..., connection = ..., html_message = ...) -> Any: ...
def send_mass_mail(datatuple, fail_silently = ..., auth_user = ..., auth_password = ..., connection = ...) -> Any: ...
