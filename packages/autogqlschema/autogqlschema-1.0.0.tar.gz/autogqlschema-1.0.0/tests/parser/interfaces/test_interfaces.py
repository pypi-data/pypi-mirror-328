from autogqlschema import _objects

from ..conftest import AlwaysEqual


def test_basic(parsed_result):
    """Can parse various basic interface definitions.

    Also check the line numbers of parsed interfaces.
    """
    args = {"arg1": "arg1 tests that arguments can be documented"}
    field_with_args = _objects.GraphQLInterfaceField(
        args,
        "interface2.field2 tests that arguments are parsed",
        "field2(arg1: Int = 0): String",
        AlwaysEqual(),
    )

    expected = _objects.GraphQLSchema(
        [
            AlwaysEqual("directiveA"),
            _objects.GraphQLInterface(
                [
                    _objects.GraphQLInterfaceField(
                        {},
                        "interface1.field1 tests parsing the simplest possible interface field definition",
                        "field1: String",
                        7,
                    ),
                ],
                "interface1 tests parsing the simplest possible interface definition",
                "interface1",
                3,
            ),
            _objects.GraphQLInterface(
                [
                    _objects.GraphQLInterfaceField(
                        {},
                        "interface2.field1 tests that directives are parsed",
                        "field1: Int @directiveA",
                        AlwaysEqual(),
                    ),
                    field_with_args,
                ],
                "interface2 tests that directives are parsed",
                "interface2 @directiveA",
                AlwaysEqual(),
            ),
        ],
        None,
        "",
    )
    assert parsed_result == expected


def test_extends_fields(parsed_result):
    """Can parse types with extensions to the list of fields."""
    expected = _objects.GraphQLSchema(
        [
            _objects.GraphQLInterface(
                [
                    _objects.GraphQLInterfaceField(
                        {},
                        "interface1.field1 tests parsing the simplest possible type field definition",
                        "field1: Int",
                        2,
                    ),
                    _objects.GraphQLInterfaceField(
                        {},
                        "interface1.field2 tests parsing the simplest possible interface extension of fields",
                        "field2: Int",
                        6,
                    ),
                ],
                None,
                "interface1",
                AlwaysEqual(),
            ),
        ],
        None,
        "",
    )
    assert parsed_result == expected


def test_extends_directives(parsed_result):
    """Can parse types with extensions to the directives."""
    expected = _objects.GraphQLSchema(
        [
            _objects.GraphQLInterface(
                [
                    AlwaysEqual("field1"),
                ],
                None,
                "interface1 @directiveA",
                AlwaysEqual(),
            ),
            AlwaysEqual("directiveA"),
        ],
        None,
        "",
    )
    assert parsed_result == expected
