from autogqlschema import _objects

from ..conftest import AlwaysEqual


def test_basic(parsed_result):
    """Can parse various basic scalar definitions.

    Also check the line numbers of parsed scalars.
    """
    expected = _objects.GraphQLSchema(
        [
            AlwaysEqual("directiveA"),
            _objects.GraphQLScalar(
                "scalar1 tests parsing the simplest possible scalar definition",
                "scalar1",
                3,
            ),
            _objects.GraphQLScalar(
                "scalar2 tests that directives are parsed",
                "scalar2 @directiveA",
                AlwaysEqual(),
            ),
        ],
        None,
        "",
    )
    assert parsed_result == expected


def test_extends(parsed_result):
    """Can parse scalar extensions."""
    expected = _objects.GraphQLSchema(
        [
            _objects.GraphQLScalar(
                "scalar1 tests that extensions are parsed",
                "scalar1 @directiveA",
                AlwaysEqual(),
            ),
            _objects.GraphQLDirective(
                {},
                AlwaysEqual(),
                "@directiveA on SCALAR",
                AlwaysEqual(),
            ),
        ],
        None,
        "",
    )
    assert parsed_result == expected
