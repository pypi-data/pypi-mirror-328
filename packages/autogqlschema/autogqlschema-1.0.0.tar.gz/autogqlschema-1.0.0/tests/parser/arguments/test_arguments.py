from autogqlschema import _objects

from ..conftest import AlwaysEqual


def test_multiple(parsed_result):
    """Can parse multiple arguments.

    Also check the line numbers of parsed objects.
    """
    args = {
        "arg1": "arg1 tests that arguments can be documented",
        "arg2": "arg2 tests that arguments can be documented",
    }
    field_with_args = _objects.GraphQLTypeField(
        args,
        "fieldA1 tests parsing with multiple arguments",
        "fieldA1(arg1: Int, arg2: input1): String",
        10,
    )

    expected = _objects.GraphQLSchema(
        [
            AlwaysEqual("input1"),
            _objects.GraphQLType(
                [
                    field_with_args,
                ],
                "A type to test different argument configurations",
                "TestArgumentType",
                6,
            ),
        ],
        None,
        "",
    )
    assert parsed_result == expected


def test_directive(parsed_result):
    """Can parse a directives on an argument."""
    args = {"arg1": None}
    field_b1 = _objects.GraphQLTypeField(
        args,
        "fieldB1 tests parsing with an argument directive",
        "fieldB1(arg1: input1 @directiveA): String",
        AlwaysEqual(),
    )

    args = {"arg1": None}
    field_b2 = _objects.GraphQLTypeField(
        args,
        "fieldB2 tests parsing with an argument directive that has const arguments",
        "fieldB2(arg1: input1 @directiveB(arg1: 1, arg2: 2)): String",
        AlwaysEqual(),
    )

    expected = _objects.GraphQLSchema(
        [
            AlwaysEqual("directiveA"),
            AlwaysEqual("directiveB"),
            AlwaysEqual("input1"),
            _objects.GraphQLType(
                [
                    field_b1,
                    field_b2,
                ],
                "A type to test different argument configurations",
                "TestArgumentType",
                AlwaysEqual(),
            ),
        ],
        None,
        "",
    )
    assert parsed_result == expected


def test_default_value(parsed_result):
    """Can parse an argument with default values."""
    args = {"arg1": None}
    fields = [
        _objects.GraphQLTypeField(
            args,
            "fieldC1 tests parsing with an argument that has a default integer value",
            "fieldC1(arg1: Int = 600): String",
            AlwaysEqual(),
        ),
        _objects.GraphQLTypeField(
            args,
            "fieldC2 tests parsing with an argument that has a default float value",
            "fieldC2(arg1: Float = 1.5): String",
            AlwaysEqual(),
        ),
        _objects.GraphQLTypeField(
            args,
            "fieldC3 tests parsing with an argument that has a default string value",
            'fieldC3(arg1: String = "mystring"): String',
            AlwaysEqual(),
        ),
        _objects.GraphQLTypeField(
            args,
            "fieldC4 tests parsing with an argument that has a default boolean value",
            "fieldC4(arg1: Boolean = true): String",
            AlwaysEqual(),
        ),
        _objects.GraphQLTypeField(
            args,
            "fieldC5 tests parsing with an argument that has a default null value",
            "fieldC5(arg1: Int = null): String",
            AlwaysEqual(),
        ),
        _objects.GraphQLTypeField(
            args,
            "fieldC6 tests parsing with an argument that has a default enum value",
            "fieldC6(arg1: enum1 = ENUMVALUE): String",
            AlwaysEqual(),
        ),
        _objects.GraphQLTypeField(
            args,
            "fieldC7 tests parsing with an argument that has a default list value",
            "fieldC7(arg1: [Int] = [1, 2]): String",
            AlwaysEqual(),
        ),
        _objects.GraphQLTypeField(
            args,
            "fieldC8 tests parsing with an argument that has a default object value",
            r"fieldC8(arg1: input1 = {one: 1, two: 2}): String",
            AlwaysEqual(),
        ),
    ]

    expected = _objects.GraphQLSchema(
        [
            AlwaysEqual("enum1"),
            AlwaysEqual("input1"),
            _objects.GraphQLType(
                fields,
                "A type to test different argument configurations",
                "TestArgumentType",
                AlwaysEqual(),
            ),
        ],
        None,
        "",
    )
    assert parsed_result == expected


def test_list_and_null(parsed_result):
    """Can parse arguments with list and null types."""
    args = {"arg1": None}
    fields = [
        _objects.GraphQLTypeField(
            args,
            "fieldD1 tests parsing with an argument that has a list type",
            "fieldD1(arg1: [input1]): String",
            AlwaysEqual(),
        ),
        _objects.GraphQLTypeField(
            args,
            "fieldD2 tests parsing with an argument that has a list type",
            "fieldD2(arg1: input1!): String",
            AlwaysEqual(),
        ),
        _objects.GraphQLTypeField(
            args,
            "fieldD3 tests parsing with an argument that has a list type with non-null values",
            "fieldD3(arg1: [input1!]): String",
            AlwaysEqual(),
        ),
    ]

    expected = _objects.GraphQLSchema(
        [
            AlwaysEqual("input1"),
            _objects.GraphQLType(
                fields,
                "A type to test different argument configurations",
                "TestArgumentType",
                AlwaysEqual(),
            ),
        ],
        None,
        "",
    )
    assert parsed_result == expected
