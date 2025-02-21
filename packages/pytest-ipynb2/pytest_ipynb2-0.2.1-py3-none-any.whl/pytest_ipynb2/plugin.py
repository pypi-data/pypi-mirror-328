"""
Pytest plugin to collect jupyter Notebooks.

- Identifies all cells which use the `%%ipytest` magic
- adds the notebook, cell and any test functions to the collection tree
- relies on pytest logic and configuration to identify test functions.

Known Issues:

- No Assertion rewriting.
"""

from __future__ import annotations

import importlib.util
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from collections.abc import Generator
    from pathlib import Path
    from types import ModuleType

from ._parser import Notebook as _ParsedNotebook

ipynb2_notebook = pytest.StashKey[_ParsedNotebook]()
ipynb2_cellid = pytest.StashKey[int]()

CELL_PREFIX = "Cell"


class Notebook(pytest.File):
    """A collector for jupyter notebooks."""

    def collect(self) -> Generator[Cell, None, None]:
        """Yield `Cell`s for all cells which contain tests."""
        parsed = _ParsedNotebook(self.path)
        for testcellid in parsed.testcells.ids():
            name = f"{CELL_PREFIX}{testcellid}"
            cell = Cell.from_parent(
                parent=self,
                name=name,
                nodeid=f"{self.nodeid}::{name}",
                path=self.path,
            )
            cell.stash[ipynb2_notebook] = parsed
            cell.stash[ipynb2_cellid] = testcellid
            yield cell


class Cell(pytest.Module):
    """
    A collector for jupyter notebook cells.

    `pytest` will recognise these cells as `pytest.Module`s and use standard collection on them as it would any other
    python module.
    """

    def __repr__(self) -> str:
        """Don't duplicate the word "Cell" in the repr."""
        return f"<{type(self).__name__} {self.stash[ipynb2_cellid]}>"

    def _getobj(self) -> ModuleType:
        notebook = self.stash[ipynb2_notebook]
        cellid = self.stash[ipynb2_cellid]

        cellsabove = "\n".join(notebook.codecells[:cellid])
        testcell = notebook.testcells[cellid]

        dummy_spec = importlib.util.spec_from_loader(f"{self.name}", loader=None)
        dummy_module = importlib.util.module_from_spec(dummy_spec)
        exec(f"{cellsabove}\n{testcell}", dummy_module.__dict__)  # noqa: S102
        return dummy_module

    def _reportinfo(self: pytest.Item) -> tuple[str, int, str | None]:
        """Override pytest which checks `.obj.__code__.co_filename` == `.path`."""
        return self.path, 0, self.getmodpath()

    def collect(self) -> Generator[pytest.Function, None, None]:
        """Replace the reportinfo method on the children, if present."""
        for item in super().collect():
            if hasattr(item, "reportinfo"):  # pragma: no branch # TODO(MusicalNinjaDad): #22 Tests grouped in Class
                item.reportinfo = self._reportinfo
            yield item


def pytest_collect_file(file_path: Path, parent: pytest.Collector) -> Notebook | None:
    """Hook implementation to collect jupyter notebooks."""
    if file_path.suffix == ".ipynb":
        return Notebook.from_parent(parent=parent, path=file_path, nodeid=file_path.name)
    return None
