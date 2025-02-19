import pathlib

import pytest

from autogqlschema._parser import Parser


@pytest.fixture
def parsed_result(request):
    """Parse the fixture for this test.

    A test called ``test_X.py::test_Y``
    will parse the file ``./Y.graphql`` relative to ``test_X.py``.
    """
    test_dir = pathlib.Path(request.node.fspath).parent
    test_name = request.node.name[len("test_") :]

    paths = [test_dir / f"{test_name}.graphql"]
    if not paths[0].exists() and (test_dir / test_name).is_dir():
        paths = sorted((test_dir / test_name).iterdir())

    return Parser.parse_from_source(*paths)


class AlwaysEqual:
    def __init__(self, _=None):
        super().__init__()

    def __eq__(self, _):
        return True
