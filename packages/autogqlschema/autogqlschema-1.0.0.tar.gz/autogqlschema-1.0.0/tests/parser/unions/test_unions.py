from autogqlschema import _objects

from ..conftest import AlwaysEqual


def test_basic(parsed_result):
    """Can parse various basic union definitions.

    Also check the line numbers of parsed unions.
    """
    expected = _objects.GraphQLSchema(
        [
            AlwaysEqual("directiveA"),
            AlwaysEqual("type1"),
            AlwaysEqual("type2"),
            _objects.GraphQLUnion(
                "union1 tests parsing the simplest possible union definition",
                "union1 = type1 | type2",
                11,
            ),
            _objects.GraphQLUnion(
                "union2 tests that directives are parsed",
                "union2 @directiveA = type1 | type2",
                AlwaysEqual(),
            ),
        ],
        None,
        "",
    )
    assert parsed_result == expected


def test_extends_types(parsed_result):
    """Can parse unions with an extension to the types."""
    expected = _objects.GraphQLSchema(
        [
            AlwaysEqual("type1"),
            AlwaysEqual("type2"),
            _objects.GraphQLUnion(
                None,
                "union1 = type1 | type2 | type3",
                AlwaysEqual(),
            ),
            AlwaysEqual("type3"),
        ],
        None,
        "",
    )
    assert parsed_result == expected


def test_extends_directives(parsed_result):
    """Can parse unions with an extension to the directives."""
    expected = _objects.GraphQLSchema(
        [
            AlwaysEqual("type1"),
            AlwaysEqual("type2"),
            _objects.GraphQLUnion(
                None,
                "union2 @directiveA = type1 | type2",
                AlwaysEqual(),
            ),
            AlwaysEqual("directiveA"),
        ],
        None,
        "",
    )
    assert parsed_result == expected
