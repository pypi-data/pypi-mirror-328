"""Tests failures are likely due to the handling of the specific case, not basic functionality."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import pytest

from pytest_ipynb2._pytester_helpers import CollectedDir, ExampleDir, add_ipytest_magic

LINESTART = "^"
LINEEND = "$"
WHITESPACE = r"\s*"


@dataclass
class ExpectedResults:
    outcomes: dict[str, int]
    """Dict of outcomes for https://docs.pytest.org/en/stable/reference/reference.html#pytest.RunResult.assert_outcomes"""
    logreport: list[tuple[str, str, int]] = field(default_factory=list)
    """Contents of logreport for -v execution. Tuple: line-title, short-form results, overall progress (%)"""
    summary: list[tuple[str, str, type[Exception] | None, str | None]] | None = field(default_factory=list)
    """
    FULL Contents of test summary info.
    
    - Tuple per line: Result, location, Exception raised, Exception message
    - Explicity pass `None` to express "No test summary" or "Element not included"
    """


parametrized = pytest.mark.parametrize(
    ["example_dir", "expected_results"],
    [
        pytest.param(
            ExampleDir(
                conftest="pytest_plugins = ['pytest_ipynb2.plugin']",
                notebooks={"passing": [add_ipytest_magic(Path("tests/assets/test_passing.py").read_text())]},
            ),
            ExpectedResults(
                outcomes={"passed": 1},
                logreport=[("passing.ipynb", ".", 100)],
                summary=None,
            ),
            id="Single Cell",
        ),
        pytest.param(
            ExampleDir(
                conftest="pytest_plugins = ['pytest_ipynb2.plugin']",
                notebooks={"failing": [add_ipytest_magic(Path("tests/assets/test_failing.py").read_text())]},
            ),
            ExpectedResults(
                outcomes={"failed": 1},
                logreport=[("failing.ipynb", "F", 100)],
                summary=[("FAILED", "failing.ipynb::Cell0::test_fails", AssertionError, None)],
            ),
            id="Failing Test",
        ),
        pytest.param(
            ExampleDir(
                conftest="pytest_plugins = ['pytest_ipynb2.plugin']",
                notebooks={"fixture": [add_ipytest_magic(Path("tests/assets/test_fixture.py").read_text())]},
            ),
            ExpectedResults(
                outcomes={"passed": 1},
            ),
            id="Test with fixture",
        ),
        pytest.param(
            ExampleDir(
                conftest="pytest_plugins = ['pytest_ipynb2.plugin']",
                notebooks={"marks": [add_ipytest_magic(Path("tests/assets/test_param.py").read_text())]},
                ini="addopts = -rx",
            ),
            ExpectedResults(
                outcomes={"passed": 1, "xfailed": 1},
                logreport=[("marks.ipynb", ".x", 100)],
                summary=[("XFAIL", "marks.ipynb::Cell0::test_params[fail]", None, "xfailed")],
            ),
            id="Test with parameters and marks",
        ),
        pytest.param(
            ExampleDir(
                conftest="pytest_plugins = ['pytest_ipynb2.plugin']",
                notebooks={
                    "autoconfig": [
                        add_ipytest_magic(Path("tests/assets/import_ipytest.py").read_text()),
                        add_ipytest_magic(Path("tests/assets/test_passing.py").read_text()),
                    ],
                },
            ),
            ExpectedResults(
                outcomes={"passed": 1},
                logreport=[("autoconfig.ipynb", ".", 100)],
            ),
            id="Notebook calls autoconfig",
        ),
        pytest.param(
            ExampleDir(
                conftest="pytest_plugins = ['pytest_ipynb2.plugin']",
                notebooks={
                    "notests": [Path("tests/assets/test_module.py").read_text()],
                },
            ),
            ExpectedResults(
                outcomes={},
            ),
            id="No ipytest cells",
        ),
        pytest.param(
            ExampleDir(
                conftest="pytest_plugins = ['pytest_ipynb2.plugin']",
                notebooks={
                    "nocells": [],
                },
            ),
            ExpectedResults(
                outcomes={},
            ),
            id="Empty notebook",
        ),
        pytest.param(
            ExampleDir(
                conftest="pytest_plugins = ['pytest_ipynb2.plugin']",
                notebooks={
                    "comments": [
                        f"# A test cell\n{add_ipytest_magic(Path('tests/assets/test_passing.py').read_text())}",
                        add_ipytest_magic(Path("tests/assets/test_failing.py").read_text()),
                    ],
                },
            ),
            ExpectedResults(
                outcomes={"passed": 1, "failed": 1},
            ),
            id="ipytest not first line",
        ),
        pytest.param(
            ExampleDir(
                conftest="pytest_plugins = ['pytest_ipynb2.plugin']",
                files=[
                    Path("tests/assets/test_module.py"),
                    Path("tests/assets/notebook.ipynb"),
                ],
            ),
            ExpectedResults(
                outcomes={"passed": 4},
                logreport=[("notebook.ipynb", "..", 50), ("test_module.py", "..", 100)],
            ),
            id="mixed file types",
        ),
        pytest.param(
            ExampleDir(
                conftest="pytest_plugins = ['pytest_ipynb2.plugin']",
                notebooks={
                    "globals": [
                        "x = 2",
                        "x = 1",
                        add_ipytest_magic(Path("tests/assets/test_globals.py").read_text()),
                        "x = 2",
                        add_ipytest_magic(Path("tests/assets/test_globals.py").read_text()),
                    ],
                },
            ),
            ExpectedResults(
                outcomes={"passed": 1, "failed": 1},
                logreport=[("globals.ipynb", ".F", 100)],
            ),
            id="cell execution order",
        ),
        pytest.param(
            ExampleDir(
                conftest="pytest_plugins = ['pytest_ipynb2.plugin']",
                files=[Path("tests/assets/test_module.py")],
            ),
            ExpectedResults(
                outcomes={"passed": 2},
                logreport=[("test_module.py", "..", 100)],
            ),
            id="output python module",
        ),
        pytest.param(
            ExampleDir(
                conftest="pytest_plugins = ['pytest_ipynb2.plugin']",
                ini="addopts = -vv",
                notebooks={
                    "two_cells": [
                        add_ipytest_magic(
                            "\n".join(
                                [
                                    Path("tests/assets/test_passing.py").read_text(),
                                    Path("tests/assets/test_failing.py").read_text(),
                                ],
                            ),
                        ),
                        add_ipytest_magic(Path("tests/assets/test_passing.py").read_text()),
                    ],
                },
            ),
            ExpectedResults(
                outcomes={"passed": 2, "failed": 1},
                logreport=[
                    ("two_cells.ipynb::Cell0::test_pass", "PASSED", 33),
                    ("two_cells.ipynb::Cell0::test_fails", "FAILED", 66),
                    ("two_cells.ipynb::Cell1::test_pass", "PASSED", 100),
                ],
                summary=[("FAILED", "two_cells.ipynb::Cell0::test_fails", AssertionError, None)],
            ),
            id="Verbose two notebooks",
        ),
    ],
    indirect=["example_dir"],
)


@parametrized
def test_results(example_dir: CollectedDir, expected_results: ExpectedResults):
    results = example_dir.pytester_instance.runpytest()
    try:
        results.assert_outcomes(**expected_results.outcomes)
    except AssertionError:
        pytest.fail(f"{results.stdout}")


@parametrized
def test_logreport(example_dir: CollectedDir, expected_results: ExpectedResults):
    if not expected_results.logreport:
        pytest.skip(reason="No expected result")

    results = example_dir.pytester_instance.runpytest()
    stdout_regexes = [
        f"{LINESTART}{re.escape(filename)}{WHITESPACE}"
        f"{re.escape(outcomes)}{WHITESPACE}"
        f"{re.escape('[')}{progress:3d}%{re.escape(']')}{WHITESPACE}{LINEEND}"
        for filename, outcomes, progress in expected_results.logreport
    ]
    results.stdout.re_match_lines(stdout_regexes, consecutive=True)


@parametrized
def test_summary(example_dir: CollectedDir, expected_results: ExpectedResults):
    if expected_results.summary is not None and not expected_results.summary:
        pytest.skip(reason="No expected result")

    results = example_dir.pytester_instance.runpytest()
    summary_regexes = ["[=]* short test summary info [=]*"]
    if expected_results.summary is not None:
        summary_regexes += [
            f"{re.escape(result)}"
            f"{WHITESPACE}{re.escape(location)}"
            f"{WHITESPACE}{re.escape('-')}{WHITESPACE}"
            f"{'' if exceptiontype is None else re.escape(exceptiontype.__name__)}"
            f"{'' if message is None else re.escape(message)}"
            f"{WHITESPACE}{LINEEND}"
            for result, location, exceptiontype, message in expected_results.summary
        ]  # message is currently not provided until we fix Assertion re-writing
        summary_regexes += ["[=]*"]
        results.stdout.re_match_lines(summary_regexes, consecutive=True)
    else:
        assert re.search(f"{LINESTART}{summary_regexes[0]}{LINEEND}", str(results.stdout), flags=re.MULTILINE) is None
