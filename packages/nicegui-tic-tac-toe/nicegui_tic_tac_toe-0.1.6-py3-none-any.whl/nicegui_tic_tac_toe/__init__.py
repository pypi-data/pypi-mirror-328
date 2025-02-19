"""nicegui_tic_tac_toe"""

from importlib.metadata import metadata

from fire import Fire as _Fire

from .tic_tac_toe import Game, game

_package_metadata = metadata(str(__package__))
__version__ = _package_metadata["Version"]
__author__ = _package_metadata.get("Author-email", "")

__all__ = ["Game", "__author__", "__version__", "main"]


def main() -> None:
    """スクリプト実行"""
    _Fire(game)
