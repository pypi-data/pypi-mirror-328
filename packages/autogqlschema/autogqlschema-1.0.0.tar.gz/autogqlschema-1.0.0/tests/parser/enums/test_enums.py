from autogqlschema import _objects

from ..conftest import AlwaysEqual


def test_basic(parsed_result):
    """Can parse various basic enum definitions.

    Also check the line numbers of parsed enums.
    """
    expected = _objects.GraphQLSchema(
        [
            AlwaysEqual("directiveA"),
            _objects.GraphQLEnum(
                [
                    _objects.GraphQLEnumValue(
                        "enum1.value1 tests parsing the simplest possible enum value definition",
                        "value1",
                        7,
                    ),
                ],
                "enum1 tests parsing the simplest possible enum definition",
                "enum1",
                3,
            ),
            _objects.GraphQLEnum(
                [
                    _objects.GraphQLEnumValue(
                        "enum2.value1 tests that directives are parsed",
                        "value1 @directiveA",
                        AlwaysEqual(),
                    ),
                ],
                "enum2 tests that directives are parsed",
                "enum2 @directiveA",
                AlwaysEqual(),
            ),
        ],
        None,
        "",
    )
    assert parsed_result == expected


def test_extends_directives(parsed_result):
    """Can parse enums extended with directives."""
    expected = _objects.GraphQLSchema(
        [
            _objects.GraphQLEnum(
                [
                    AlwaysEqual("value1"),
                ],
                None,
                "enum2 @directiveA",
                AlwaysEqual(),
            ),
            AlwaysEqual("directiveA"),
        ],
        None,
        "",
    )
    assert parsed_result == expected


def test_extends_values(parsed_result):
    """Can parse enums extended with extra values."""
    expected = _objects.GraphQLSchema(
        [
            _objects.GraphQLEnum(
                [
                    _objects.GraphQLEnumValue(
                        "enum1.value1 tests parsing the simplest possible enum value definition",
                        "value1",
                        AlwaysEqual(),
                    ),
                    _objects.GraphQLEnumValue(
                        "enum1.value2 tests parsing the simplest possible enum extension of values",
                        "value2",
                        AlwaysEqual(),
                    ),
                ],
                None,
                "enum1",
                AlwaysEqual(),
            ),
        ],
        None,
        "",
    )
    assert parsed_result == expected
