from autogqlschema import _objects

from ..conftest import AlwaysEqual


def test_basic(parsed_result):
    """Can parse various basic directive definitions.

    Also check the line numbers of parsed directives.
    """
    args = {"arg1": "arg1 tests that arguments can be documented"}
    directive_with_args = _objects.GraphQLDirective(
        args,
        "directive3 tests that arguments are parsed",
        "@directive3(arg1: input1) on SCALAR",
        AlwaysEqual(),
    )

    expected = _objects.GraphQLSchema(
        [
            AlwaysEqual("input1"),
            _objects.GraphQLDirective(
                {},
                "directive1 tests parsing the simplest possible directive definition",
                "@directive1 on SCHEMA",
                6,
            ),
            _objects.GraphQLDirective(
                {},
                "directive2 tests parsing with multiple type system directive locations",
                "@directive2 on FIELD_DEFINITION | ARGUMENT_DEFINITION",
                AlwaysEqual(),
            ),
            directive_with_args,
        ],
        None,
        "",
    )
    assert parsed_result == expected
