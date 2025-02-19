from autogqlschema import _objects

from ..conftest import AlwaysEqual


def test_basic(parsed_result):
    """Can parse various basic input definitions.

    Also check the line numbers of parsed inputs.
    """
    expected = _objects.GraphQLSchema(
        [
            AlwaysEqual("directiveA"),
            _objects.GraphQLInput(
                [
                    _objects.GraphQLInputField(
                        "input1.field1 tests parsing the simplest possible input field definition",
                        "field1: Float",
                        7,
                    ),
                ],
                "input1 tests parsing the simplest possible input definition",
                "input1",
                3,
            ),
            _objects.GraphQLInput(
                [
                    _objects.GraphQLInputField(
                        "input2.field1 tests that directives are parsed",
                        "field1: Int @directiveA",
                        AlwaysEqual(),
                    ),
                    _objects.GraphQLInputField(
                        "input2.field2 tests that default values are parsed",
                        'field2: String = "defaultvaluefield2"',
                        AlwaysEqual(),
                    ),
                ],
                "input2 tests that directives are parsed",
                "input2 @directiveA",
                AlwaysEqual(),
            ),
        ],
        None,
        "",
    )
    assert parsed_result == expected


def test_extends_fields(parsed_result):
    """Can parse input objects with extensions to the list of fields."""
    expected = _objects.GraphQLSchema(
        [
            _objects.GraphQLInput(
                [
                    _objects.GraphQLInputField(
                        "input1.field1 tests parsing the simplest possible input field definition",
                        "field1: Int",
                        2,
                    ),
                    _objects.GraphQLInputField(
                        "input1.field2 tests parsing the simplest possible input extension of fields",
                        "field2: Int",
                        6,
                    ),
                ],
                None,
                "input1",
                AlwaysEqual(),
            ),
        ],
        None,
        "",
    )
    assert parsed_result == expected


def test_extends_directives(parsed_result):
    """Can parse input objects with extensions to the directives."""
    expected = _objects.GraphQLSchema(
        [
            _objects.GraphQLInput(
                [
                    AlwaysEqual("field1"),
                ],
                None,
                "input1 @directiveA",
                AlwaysEqual(),
            ),
            AlwaysEqual("directiveA"),
        ],
        None,
        "",
    )
    assert parsed_result == expected
