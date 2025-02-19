# (generated with --quick)

import mail.backends.base
import sys
import threading
from typing import Any, Optional

BaseEmailBackend: type[mail.backends.base.BaseEmailBackend]

class EmailBackend(mail.backends.base.BaseEmailBackend):
    _lock: threading._RLock
    stream: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def send_messages(self, email_messages) -> Optional[int]: ...
    def write_message(self, message) -> None: ...
