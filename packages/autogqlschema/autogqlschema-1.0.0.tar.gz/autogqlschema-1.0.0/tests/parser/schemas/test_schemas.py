from autogqlschema import _objects

from ..conftest import AlwaysEqual


def test_basic(parsed_result):
    """Can parse the most basic schema definition.

    Also check the line numbers of parsed objects.
    """
    expected = _objects.GraphQLSchema(
        [_objects.GraphQLType(AlwaysEqual(), None, "MyQueryRootType1", 5)], None, ""
    )
    expected.query_type = "MyQueryRootType1"
    assert parsed_result == expected


def test_all_root_types(parsed_result):
    """Can parse all root types."""
    expected = _objects.GraphQLSchema(AlwaysEqual(), None, "@directive1 @directive2")
    expected.query_type = "MyQueryRootType1"
    expected.mutation_type = "MyMutationRootType1"
    expected.subscription_type = "MySubscriptionRootType1"
    assert parsed_result == expected


def test_extends(parsed_result):
    """Can parse an extended schema with directives on the extension."""
    expected = _objects.GraphQLSchema(AlwaysEqual(), None, "@directive1 @directive2")
    expected.query_type = "MyQueryRootType1"
    expected.mutation_type = "MyMutationRootType1"
    expected.subscription_type = "MySubscriptionRootType1"
    assert parsed_result == expected


def test_extends_reversed(parsed_result):
    """Can parse an extended schema in reverse order of definition."""
    expected = _objects.GraphQLSchema(AlwaysEqual(), None, "@directive1 @directive2")
    expected.query_type = "MyQueryRootType1"
    expected.mutation_type = "MyMutationRootType1"
    expected.subscription_type = "MySubscriptionRootType1"
    assert parsed_result == expected
