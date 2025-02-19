"""Book List"""

from importlib.metadata import metadata

import fire

from .main import run
from .models import Author, Book
from .ui import AuthorList, BookList, ListBase

_package_metadata = metadata(str(__package__))
__version__ = _package_metadata["Version"]
__author__ = _package_metadata.get("Author-email", "")

__all__ = [
    "Author",
    "AuthorList",
    "Book",
    "BookList",
    "ListBase",
    "__author__",
    "__version__",
    "run",
]


def main() -> None:
    """スクリプト実行"""
    fire.Fire(run)
