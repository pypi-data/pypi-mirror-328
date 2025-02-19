from autogqlschema import _objects

from ..conftest import AlwaysEqual


def test_basic(parsed_result):
    """Can parse various basic type definitions.

    Also check the line numbers of parsed types.
    """
    args = {"arg1": "arg1 tests that arguments can be documented"}
    field_with_args = _objects.GraphQLTypeField(
        args,
        "type2.field2 tests that arguments are parsed",
        "field2(arg1: Int = 0): String",
        AlwaysEqual(),
    )

    expected = _objects.GraphQLSchema(
        [
            AlwaysEqual("directiveA"),
            _objects.GraphQLType(
                [
                    _objects.GraphQLTypeField(
                        {},
                        "type1.field1 tests parsing the simplest possible type field definition",
                        "field1: Int",
                        7,
                    ),
                ],
                "type1 tests parsing the simplest possible type definition",
                "type1",
                3,
            ),
            _objects.GraphQLType(
                [
                    _objects.GraphQLTypeField(
                        {},
                        "type2.field1 tests that directives are parsed",
                        "field1: Int @directiveA",
                        AlwaysEqual(),
                    ),
                    field_with_args,
                ],
                "type2 tests that directives are parsed",
                "type2 @directiveA",
                AlwaysEqual(),
            ),
        ],
        None,
        "",
    )
    assert parsed_result == expected


def test_inherits(parsed_result):
    """Can parse types with inheritance."""
    expected = _objects.GraphQLSchema(
        [
            AlwaysEqual("interface1"),
            AlwaysEqual("interface2"),
            _objects.GraphQLType(
                [
                    _objects.GraphQLTypeField(
                        {},
                        AlwaysEqual(),
                        "field1: Int",
                        AlwaysEqual(),
                    ),
                ],
                "type1 tests parsing a single inherited type",
                "type1 implements interface1",
                AlwaysEqual(),
            ),
            _objects.GraphQLType(
                [
                    AlwaysEqual(),
                ],
                "type2 tests parsing multiple inherited types",
                "type2 implements interface1 & interface2",
                AlwaysEqual(),
            ),
        ],
        None,
        "",
    )
    assert parsed_result == expected


def test_extends_inheritance(parsed_result):
    """Can parse types with inheritance."""
    expected = _objects.GraphQLSchema(
        [
            AlwaysEqual("interface1"),
            _objects.GraphQLType(
                [
                    AlwaysEqual(),
                ],
                "type1 tests parsing extensions to inheritance",
                "type1 implements interface1 & interface2",
                AlwaysEqual(),
            ),
            AlwaysEqual("interface2"),
        ],
        None,
        "",
    )
    assert parsed_result == expected


def test_extends_fields(parsed_result):
    """Can parse types with extensions to the list of fields."""
    expected = _objects.GraphQLSchema(
        [
            _objects.GraphQLType(
                [
                    _objects.GraphQLTypeField(
                        {},
                        "type1.field1 tests parsing the simplest possible type field definition",
                        "field1: Int",
                        2,
                    ),
                    _objects.GraphQLTypeField(
                        {},
                        "type1.field2 tests parsing the simplest possible type extension of fields",
                        "field2: Int",
                        6,
                    ),
                ],
                None,
                "type1",
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
            _objects.GraphQLType(
                [
                    AlwaysEqual("field1"),
                ],
                None,
                "type1 @directiveA",
                AlwaysEqual(),
            ),
            AlwaysEqual("directiveA"),
        ],
        None,
        "",
    )
    assert parsed_result == expected
