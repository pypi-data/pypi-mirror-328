from pathlib import Path

import nbformat
import pytest

from pytest_ipynb2.pytester_helpers import CollectedDir, ExampleDir

tests = [
    pytest.param(
        ExampleDir(
            [Path("tests/assets/test_module.py").absolute()],
        ),
        {"test_module.py": None},
        id="One File",
    ),
    pytest.param(
        ExampleDir(
            [Path("tests/assets/test_module.py").absolute(), Path("tests/assets/test_othermodule.py").absolute()],
        ),
        {
            "test_module.py": None,
            "test_othermodule.py": None,
        },
        id="Two files",
    ),
    pytest.param(
        ExampleDir(
            [Path("tests/assets/notebook.ipynb").absolute()],
        ),
        {"notebook.ipynb": None},
        id="Copied Notebook",
    ),
    pytest.param(
        ExampleDir(
            notebooks={"generated": [Path("tests/assets/passing_test.py").read_text()]},
        ),
        {
            "generated.ipynb": [
                "\n".join(  # noqa: FLY002
                    [
                        r"%%ipytest",
                        "",
                        "def test_pass():",
                        "    assert True",
                    ],
                ),
            ],
        },
        id="Generated Notebook",
    ),
    pytest.param(
        ExampleDir(
            notebooks={
                "generated": [
                    Path("tests/assets/import_ipytest.py").read_text(),
                    Path("tests/assets/passing_test.py").read_text(),
                ],
            },
        ),
        {
            "generated.ipynb": [
                "\n".join(  # noqa: FLY002
                    [
                        "import ipytest",
                        "ipytest.autoconfig()",
                        "",
                    ],
                ),
                "\n".join(  # noqa: FLY002
                    [
                        r"%%ipytest",
                        "",
                        "def test_pass():",
                        "    assert True",
                    ],
                ),
            ],
        },
        id="Generated Notebook 2 cells",
    ),
]


@pytest.mark.parametrize(
    ["example_dir", "expected_files"],
    tests,
    indirect=["example_dir"],
)
def test_filesexist(example_dir: CollectedDir, expected_files: list[str]):
    tmp_path = example_dir.pytester_instance.path
    files_exist = ((tmp_path / expected_file).exists() for expected_file in expected_files)
    assert all(files_exist), f"These are not the files you are looking for: {list(tmp_path.iterdir())}"


@pytest.mark.parametrize(
    ["example_dir", "expected_files"],
    tests,
    indirect=["example_dir"],
)
def test_filecontents(example_dir: CollectedDir, expected_files: dict[str, list[str]]):
    tmp_path = example_dir.pytester_instance.path
    for filename, expected_contents in expected_files.items():
        if expected_contents is not None:
            nb = nbformat.read(fp=tmp_path / filename, as_version=nbformat.NO_CONVERT)
            assert [cell.source for cell in nb.cells] == expected_contents
