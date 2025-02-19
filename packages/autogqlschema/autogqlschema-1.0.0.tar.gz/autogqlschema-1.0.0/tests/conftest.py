from autogqlschema import _objects


def _explain(left, right):
    result = []

    if not (
        isinstance(left, _objects.GraphQLObject)
        and isinstance(right, _objects.GraphQLObject)
    ):
        return []

    if not type(left) == type(right):
        return [
            f"because left is a {type(left).__name__} and right is a {type(right).__name__}"
        ]

    if isinstance(left, _objects.GraphQLObjectWithChildren):
        if left.children != right.children:
            len_left = len(left.children)
            len_right = len(right.children)
            for i in range(min(len_left, len_right)):
                if left.children[i] != right.children[i]:
                    left_child = left.children[i]
                    right_child = right.children[i]

                    result.append(
                        f"because children differ at index {i} diff: {left_child!r} != {right_child!r}"
                    )
                    nested_lines = _explain(left_child, right_child)
                    for nested_line in nested_lines:
                        result.append(f"  {nested_line}")
                    break
            else:
                len_diff = len_left - len_right
                if len_diff:
                    result.append(
                        f"because left has {len_left} children and right has {len_right}"
                    )

    if left.description != right.description:
        if result:
            result.append(
                f"and descriptions differ: {repr(left.description)} != {repr(right.description)}"
            )
        else:
            result.append(
                f"because descriptions differ: {repr(left.description)} != {repr(right.description)}"
            )

    if left.signature != right.signature:
        if result:
            result.append(
                f"and signatures differ: {repr(left.signature)} != {repr(right.signature)}"
            )
        else:
            result.append(
                f"because signatures differ: {repr(left.signature)} != {repr(right.signature)}"
            )

    if left.line != right.line:
        if result:
            result.append(
                f"and source line numbers differ: {repr(left.line)} != {repr(right.line)}"
            )
        else:
            result.append(
                f"because source line numbers differ: {repr(left.line)} != {repr(right.line)}"
            )

    if isinstance(left, _objects.GraphQLSchema):
        if left.name != right.name:
            if result:
                result.append(
                    f"and names differ: {repr(left.name)} != {repr(right.name)}"
                )
            else:
                result.append(
                    f"because names differ: {repr(left.name)} != {repr(right.name)}"
                )

        if left.query_type != right.query_type:
            if result:
                result.append(
                    f"and query types differ: {repr(left.query_type)} != {repr(right.query_type)}"
                )
            else:
                result.append(
                    f"because query types differ: {repr(left.query_type)} != {repr(right.query_type)}"
                )

        if left.mutation_type != right.mutation_type:
            if result:
                result.append(
                    f"and mutation types differ: {repr(left.mutation_type)} != {repr(right.mutation_type)}"
                )
            else:
                result.append(
                    f"because mutation types differ: {repr(left.mutation_type)} != {repr(right.mutation_type)}"
                )

        if left.subscription_type != right.subscription_type:
            if result:
                result.append(
                    f"and subscription types differ: {repr(left.subscription_type)} != {repr(right.subscription_type)}"
                )
            else:
                result.append(
                    f"because subscription types differ: {repr(left.subscription_type)} != {repr(right.subscription_type)}"
                )
    elif isinstance(left, _objects.GraphQLObjectWithArgs):
        if left.args != right.args:
            if result:
                result.append(
                    f"and arguments differ: {repr(left.args)} != {repr(right.args)}"
                )
            else:
                result.append(
                    f"because arguments differ: {repr(left.args)} != {repr(right.args)}"
                )

    return result


def pytest_assertrepr_compare(op, left, right):
    if (
        isinstance(left, _objects.GraphQLObject)
        and isinstance(right, _objects.GraphQLObject)
        and op == "=="
    ):
        summary = f"{repr(left)} {op} {repr(right)}"
        explanation = _explain(left, right)

        if not explanation:
            return None

        return [summary] + explanation
