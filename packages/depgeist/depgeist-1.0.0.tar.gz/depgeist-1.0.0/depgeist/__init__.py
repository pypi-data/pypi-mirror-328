"""
Depgeist: A smart dependency checker for Python projects.
"""

__version__ = "1.0.0"

from .scanner import scan_project
from .checker import check_dependencies
from .updater import suggest_updates