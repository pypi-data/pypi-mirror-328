# (generated with --quick)

import ctypes
import errno
import os
import signal
import sys

ON_WINDOWS: bool

class ProcessManager:
    def kill(self, pid) -> None: ...
    def terminate(self, pid) -> None: ...
