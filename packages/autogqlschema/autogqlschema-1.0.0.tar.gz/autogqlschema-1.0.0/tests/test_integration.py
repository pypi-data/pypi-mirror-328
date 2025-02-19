import os
import pathlib
import re
import shutil

import bs4
import pytest
from sphinx.application import Sphinx


def rebuild(**kwargs) -> None:
    """Build the documentation.

    Documentation is output to ``./_build/html``.
    """
    app = Sphinx(
        srcdir=".",
        confdir=".",
        outdir="_build/html",
        doctreedir="_build/.doctrees",
        buildername="html",
        warningiserror=True,
        confoverrides={"suppress_warnings": ["app"]},
        **kwargs,
    )
    app.build()


@pytest.fixture(scope="class")
def builder(tmp_path_factory):
    cwd = pathlib.Path.cwd()

    def build(test_name, extra_content="", **kwargs):
        dest = tmp_path_factory.mktemp(test_name)
        test_file_name = f"{test_name}.graphql"
        test_file = pathlib.Path("tests") / "fixtures" / test_file_name
        shutil.copy(test_file, dest)
        shutil.copy(pathlib.Path("tests") / "fixtures" / "conf.py", dest)

        with (dest / "index.rst").open("w") as out_f:
            out_f.write(f"Schema\n")
            out_f.write(f"------\n")
            out_f.write(f"\n")
            out_f.write(f".. autogqlschema:: schema1\n")
            out_f.write(f"   :debug:\n")
            out_f.write(f"   :source-files: {test_file_name}\n\n")
            if extra_content:
                out_f.write(extra_content)

        os.chdir(dest)
        rebuild(**kwargs)

    yield build

    os.chdir(cwd)


def signature_text(soup: bs4.BeautifulSoup):
    # Strip the anchor character off the end
    result = soup.get_text()[:-1]
    # Strip the leading newline character that doesn't get displayed to users
    result = result.strip()
    # Condense double spaces created by HTML output quirks or `.get_text()` quirks
    result = re.sub("  ", " ", result)
    return result


class TestArguments:
    @pytest.fixture(scope="class")
    def soup(self, builder):
        builder("arguments")
        with (pathlib.Path("_build") / "html" / "index.html").open() as in_f:
            return bs4.BeautifulSoup(in_f, "html.parser")

    def test_multiple_arguments(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.TestArgumentType.fieldA1")
        assert signature_text(sig) == "fieldA1(arg1: Int, arg2: input1): String"

    def test_argument_fields(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.TestArgumentType.fieldA1")
        links = sig.parent.find("ul").find_all("li")
        assert len(links) == 2
        int_link, input_link = links
        assert int_link.get_text().startswith("arg1")
        assert int_link.get_text().endswith(
            "arg1 tests that arguments can be documented"
        )
        assert not soup.find("blockquote")
        assert input_link.get_text().startswith("arg2")
        assert input_link.get_text().endswith(
            "arg2 tests that arguments can be documented.\n"
            "It also tests that multiline docstrings are formatted correctly.\n"
        )

    def test_type_is_linked(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.TestArgumentType.fieldA1")
        link = sig.a
        assert link, "Argument type did not resolve to a valid hyperlink"
        assert link.get_text() == "input1"

    def test_with_directive(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.TestArgumentType.fieldB1")
        assert signature_text(sig) == "fieldB1(arg1: input1 @directiveA): String"

    def test_with_directive_const_arguments(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.TestArgumentType.fieldB2")
        assert (
            signature_text(sig)
            == "fieldB2(arg1: input1 @directiveB(arg1: 1, arg2: 2)): String"
        )

    def test_directive_is_linked(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.TestArgumentType.fieldB1")
        links = sig.find_all("a")
        assert len(links) == 3
        assert links[1], "Argument directive did not resolve to a valid hyperlink"
        assert links[1].get_text() == "directiveA"

    def test_with_default_int_value(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.TestArgumentType.fieldC1")
        assert signature_text(sig) == "fieldC1(arg1: Int = 600): String"

    def test_with_default_float_value(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.TestArgumentType.fieldC2")
        assert signature_text(sig) == "fieldC2(arg1: Float = 1.5): String"

    def test_with_default_string_value(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.TestArgumentType.fieldC3")
        assert signature_text(sig) == 'fieldC3(arg1: String = "mystring"): String'

    def test_with_default_boolean_value(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.TestArgumentType.fieldC4")
        assert signature_text(sig) == "fieldC4(arg1: Boolean = true): String"

    def test_with_default_null_value(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.TestArgumentType.fieldC5")
        assert signature_text(sig) == "fieldC5(arg1: Int = null): String"

    def test_with_default_enum_value(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.TestArgumentType.fieldC6")
        assert signature_text(sig) == "fieldC6(arg1: enum1 = ENUMVALUE): String"

    def test_with_default_list_value(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.TestArgumentType.fieldC7")
        assert signature_text(sig) == "fieldC7(arg1: [Int] = [1, 2]): String"

    def test_with_default_object_value(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.TestArgumentType.fieldC8")
        assert signature_text(sig) == "fieldC8(arg1: input1 = {one: 1, two: 2}): String"

    def test_with_list_type(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.TestArgumentType.fieldD1")
        assert signature_text(sig) == "fieldD1(arg1: [input1]): String"
        link = sig.a
        assert link, "Nested type did not resolve to a valid hyperlink"
        assert link.get_text() == "input1"

    def test_with_non_null_type(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.TestArgumentType.fieldD2")
        assert signature_text(sig) == "fieldD2(arg1: input1!): String"
        link = sig.a
        assert link, "Non-null type did not resolve to a valid hyperlink"
        assert link.get_text() == "input1"

    def test_with_list_type_non_null_values(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.TestArgumentType.fieldD3")
        assert signature_text(sig) == "fieldD3(arg1: [input1!]): String"
        link = sig.a
        assert link, "Nested non-null type did not resolve to a valid hyperlink"
        assert link.get_text() == "input1"


class TestDirectives:
    @pytest.fixture(scope="class")
    def soup(self, builder):
        extra_content = "Roles\n-----\n\n:gql:directive:`schema1.directive1`\n"
        builder("directives", extra_content=extra_content)
        with (pathlib.Path("_build") / "html" / "index.html").open() as in_f:
            return bs4.BeautifulSoup(in_f, "html.parser")

    def test_simple_parse(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.directive1")
        assert signature_text(sig) == "directive @directive1 on SCHEMA"

    def test_multi_location(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.directive2")
        assert (
            signature_text(sig)
            == "directive @directive2 on FIELD_DEFINITION | ARGUMENT_DEFINITION"
        )

    def test_with_argument(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.directive3")
        assert (
            signature_text(sig)
            == "directive @directive3(arg1: input1, arg2: input1) on SCALAR"
        )

    def test_role(self, soup: bs4.BeautifulSoup):
        links = soup.find(id="roles").find_all("a", "reference")
        assert len(links) == 1
        link = links[0]
        assert link.get_text() == "schema1.directive1"

    def test_docstrings(self, soup: bs4.BeautifulSoup):
        assert not soup.find("blockquote")

        sig = soup.find(id="schema1.directive3")
        docstring = sig.parent.dd
        assert docstring.get_text().startswith(
            "directive3 tests that arguments are parsed.\n"
            "It also tests that multiline docstrings are formatted correctly."
        )

        links = sig.parent.find("ul").find_all("li")
        assert len(links) == 2
        arg1_link, arg2_link = links
        assert arg1_link.get_text().startswith("arg1")
        assert arg1_link.get_text().endswith(
            "arg1 tests that arguments can be documented."
        )
        assert arg2_link.get_text().startswith("arg2")
        assert arg2_link.get_text().endswith(
            "arg2 tests that arguments can be documented.\n"
            "It also tests that multiline docstrings are formatted correctly.\n"
        )


class TestEnums:
    @pytest.fixture(scope="class")
    def soup(self, builder):
        extra_content = (
            "Roles\n"
            "-----\n"
            "\n"
            ":gql:enum:`schema1.enum1`\n"
            "\n"
            ":gql:enum:value:`schema1.enum1.value1`\n"
        )
        builder("enums", extra_content=extra_content)
        with (pathlib.Path("_build") / "html" / "index.html").open() as in_f:
            return bs4.BeautifulSoup(in_f, "html.parser")

    def test_simple_parse(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.enum1")
        assert signature_text(sig) == "enum enum1"

        sig = soup.find(id="schema1.enum1.value1")
        assert signature_text(sig) == "value1"

    def test_with_directive(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.enum2")
        assert signature_text(sig) == "enum enum2 @directiveA"

        sig = soup.find(id="schema1.enum2.value1")
        assert signature_text(sig) == "value1 @directiveA"

    def test_role(self, soup: bs4.BeautifulSoup):
        links = soup.find(id="roles").find_all("a", "reference")
        assert len(links) == 2
        enum_link, value_link = links
        assert enum_link.get_text() == "schema1.enum1"
        assert value_link.get_text() == "schema1.enum1.value1"

    def test_docstrings(self, soup: bs4.BeautifulSoup):
        assert not soup.find("blockquote")

        sig = soup.find(id="schema1.enum2")
        docstring = sig.parent.dd
        assert docstring.get_text().startswith(
            "enum2 tests that directives are parsed.\n"
            "It also tests that multiline docstrings are formatted correctly."
        )

        sig = soup.find(id="schema1.enum2.value1")
        docstring = sig.parent.dd
        assert docstring.get_text().endswith(
            "enum2.value1 tests that directives are parsed.\n"
            "It also tests that multiline docstrings are formatted correctly.\n"
        )


class TestInputs:
    @pytest.fixture(scope="class")
    def soup(self, builder):
        extra_content = (
            "Roles\n"
            "-----\n"
            "\n"
            ":gql:input:`schema1.input1`"
            "\n"
            ":gql:input:field:`schema1.input1.field1`\n"
        )
        builder("inputs", extra_content=extra_content)
        with (pathlib.Path("_build") / "html" / "index.html").open() as in_f:
            return bs4.BeautifulSoup(in_f, "html.parser")

    def test_simple_parse(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.input1")
        assert signature_text(sig) == "input input1"

        sig = soup.find(id="schema1.input1.field1")
        assert signature_text(sig) == "field1: Float"

    def test_with_directive(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.input2")
        assert signature_text(sig) == "input input2 @directiveA"

        sig = soup.find(id="schema1.input2.field1")
        assert signature_text(sig) == "field1: Int @directiveA"

    def test_with_default_value(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.input2.field2")
        assert signature_text(sig) == 'field2: String = "defaultvaluefield2"'

    def test_role(self, soup: bs4.BeautifulSoup):
        links = soup.find(id="roles").find_all("a", "reference")
        assert len(links) == 2
        input_link, field_link = links
        assert input_link.get_text() == "schema1.input1"
        assert field_link.get_text() == "schema1.input1.field1"

    def test_docstrings(self, soup: bs4.BeautifulSoup):
        assert not soup.find("blockquote")

        sig = soup.find(id="schema1.input2")
        docstring = sig.parent.dd
        assert docstring.get_text().startswith(
            "input2 tests that directives are parsed.\n"
            "It also tests that multiline docstrings are formatted correctly."
        )

        sig = soup.find(id="schema1.input2.field1")
        docstring = sig.parent.dd
        assert docstring.get_text().endswith(
            "input2.field1 tests that directives are parsed.\n"
            "It also tests that multiline docstrings are formatted correctly.\n"
        )


class TestInterfaces:
    @pytest.fixture(scope="class")
    def soup(self, builder):
        extra_content = (
            "Roles\n"
            "-----\n"
            "\n"
            ":gql:interface:`schema1.interface1`\n"
            "\n"
            ":gql:interface:field:`schema1.interface1.field1`\n"
        )
        builder("interfaces", extra_content=extra_content)
        with (pathlib.Path("_build") / "html" / "index.html").open() as in_f:
            return bs4.BeautifulSoup(in_f, "html.parser")

    def test_simple_parse(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.interface1")
        assert signature_text(sig) == "interface interface1"

        sig = soup.find(id="schema1.interface1.field1")
        assert signature_text(sig) == "field1: String"

    def test_with_directive(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.interface2")
        assert signature_text(sig) == "interface interface2 @directive1"

        sig = soup.find(id="schema1.interface2.field1")
        assert signature_text(sig) == "field1: Int @directive1"

    def test_with_default_value(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.interface2.field2")
        assert signature_text(sig) == "field2(arg1: Int = 0): String"

    def test_role(self, soup: bs4.BeautifulSoup):
        links = soup.find(id="roles").find_all("a", "reference")
        assert len(links) == 2
        input_link, field_link = links
        assert input_link.get_text() == "schema1.interface1"
        assert field_link.get_text() == "schema1.interface1.field1"

    def test_docstrings(self, soup: bs4.BeautifulSoup):
        assert not soup.find("blockquote")

        sig = soup.find(id="schema1.interface2")
        docstring = sig.parent.dd
        assert docstring.get_text().startswith(
            "interface2 tests that directives are parsed.\n"
            "It also tests that multiline docstrings are formatted correctly."
        )

        sig = soup.find(id="schema1.interface2.field1")
        docstring = sig.parent.dd
        assert docstring.get_text().endswith(
            "interface2.field1 tests that directives are parsed.\n"
            "It also tests that multiline docstrings are formatted correctly.\n"
        )


class TestScalars:
    @pytest.fixture(scope="class")
    def soup(self, builder):
        extra_content = "Roles\n-----\n\n:gql:scalar:`schema1.scalar1`\n"
        builder("scalars", extra_content=extra_content)
        with (pathlib.Path("_build") / "html" / "index.html").open() as in_f:
            return bs4.BeautifulSoup(in_f, "html.parser")

    def test_simple_parse(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.scalar1")
        assert signature_text(sig) == "scalar scalar1"

    def test_with_directive(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.scalar2")
        assert signature_text(sig) == "scalar scalar2 @directive1"

    def test_role(self, soup: bs4.BeautifulSoup):
        links = soup.find(id="roles").find_all("a", "reference")
        assert len(links) == 1
        link = links[0]
        assert link.get_text() == "schema1.scalar1"

    def test_docstrings(self, soup: bs4.BeautifulSoup):
        assert not soup.find("blockquote")

        sig = soup.find(id="schema1.scalar2")
        docstring = sig.parent.dd
        assert docstring.get_text().startswith(
            "scalar2 tests that directives are parsed.\n"
            "It also tests that multiline docstrings are formatted correctly."
        )


class TestSchemas:
    @pytest.fixture(scope="class")
    def soup(self, builder):
        extra_content = "Roles\n-----\n\n:gql:schema:`schema1`\n"
        builder("schemas_basic", extra_content=extra_content)
        with (pathlib.Path("_build") / "html" / "index.html").open() as in_f:
            return bs4.BeautifulSoup(in_f, "html.parser")

    def test_simple_parse(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1")
        assert signature_text(sig) == "schema"

        fields = sig.parent.find("ul").find_all("li")
        assert len(fields) == 3
        query_field, mutation_field, subscription_field = fields
        assert query_field.get_text().startswith("query")
        assert query_field.find("a").get_text() == "MyQueryRootType"
        assert mutation_field.get_text().startswith("mutation")
        assert mutation_field.find("a").get_text() == "MyMutationRootType"
        assert subscription_field.get_text().startswith("subscription")
        assert subscription_field.find("a").get_text() == "MySubscriptionRootType"

    def test_role(self, soup: bs4.BeautifulSoup):
        links = soup.find(id="roles").find_all("a", "reference")
        assert len(links) == 1
        link = links[0]
        assert link.get_text() == "schema1"


class TestSchemasDirectives:
    @pytest.fixture(scope="class")
    def soup(self, builder):
        builder("schemas_directives")
        with (pathlib.Path("_build") / "html" / "index.html").open() as in_f:
            return bs4.BeautifulSoup(in_f, "html.parser")

    def test_with_directive(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1")
        assert signature_text(sig) == "schema @directive1 @directive2"

    def test_docstrings(self, soup: bs4.BeautifulSoup):
        assert not soup.find("blockquote")

        sig = soup.find(id="schema1")
        docstring = sig.parent.dd
        assert docstring.get_text().startswith(
            "schema1 tests that directives are parsed, and operation types are rendered and linked.\n"
            "It also tests that multiline docstrings are formatted correctly."
        )


class TestSchemasOptionalOptypes:
    @pytest.fixture(scope="class")
    def soup(self, builder):
        builder("schemas_optional_optypes")
        with (pathlib.Path("_build") / "html" / "index.html").open() as in_f:
            return bs4.BeautifulSoup(in_f, "html.parser")

    def test_optional_optypes(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1")

        fields = sig.parent.find("ul").find_all("li")
        assert len(fields) == 1
        query_field = fields[0]
        assert query_field.get_text().startswith("query")
        assert query_field.find("span").get_text() == "MyQueryRootType"


class TestTypeObjects:
    @pytest.fixture(scope="class")
    def soup(self, builder):
        extra_content = (
            "Roles\n"
            "-----\n"
            "\n"
            ":gql:type:`schema1.type1`\n"
            "\n"
            ":gql:type:field:`schema1.type1.field1`\n"
        )
        builder("type_objects", extra_content=extra_content)
        with (pathlib.Path("_build") / "html" / "index.html").open() as in_f:
            return bs4.BeautifulSoup(in_f, "html.parser")

    def test_simple_parse(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.type1")
        assert signature_text(sig) == "type type1"

        sig = soup.find(id="schema1.type1.field1")
        assert signature_text(sig) == "field1: Int"

    def test_with_directive(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.type2")
        assert signature_text(sig) == "type type2 @directive1"

        sig = soup.find(id="schema1.type2.field1")
        assert signature_text(sig) == "field1: Int @directive1"

    def test_with_default_value(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.type2.field2")
        assert signature_text(sig) == "field2(arg1: Int = 0): String"

    def test_role(self, soup: bs4.BeautifulSoup):
        links = soup.find(id="roles").find_all("a", "reference")
        assert len(links) == 2
        input_link, field_link = links
        assert input_link.get_text() == "schema1.type1"
        assert field_link.get_text() == "schema1.type1.field1"

    def test_docstrings(self, soup: bs4.BeautifulSoup):
        assert not soup.find("blockquote")

        sig = soup.find(id="schema1.type2")
        docstring = sig.parent.dd
        assert docstring.get_text().startswith(
            "type2 tests that directives are parsed.\n"
            "It also tests that multiline docstrings are formatted correctly."
        )

        sig = soup.find(id="schema1.type2.field1")
        docstring = sig.parent.dd
        assert docstring.get_text().endswith(
            "type2.field1 tests that directives are parsed.\n"
            "It also tests that multiline docstrings are formatted correctly.\n"
        )

        sig = soup.find(id="schema1.type2.field2")
        links = sig.parent.find("ul").find_all("li")
        assert len(links) == 1
        arg1_link = links[0]
        assert arg1_link.get_text().startswith("arg1")
        assert arg1_link.get_text().endswith(
            "arg1 tests that arguments can be documented.\n"
            "It also tests that multiline docstrings are formatted correctly.\n"
        )


class TestUnions:
    @pytest.fixture(scope="class")
    def soup(self, builder):
        extra_content = "Roles\n-----\n\n:gql:union:`schema1.union1`\n"
        builder("unions", extra_content=extra_content)
        with (pathlib.Path("_build") / "html" / "index.html").open() as in_f:
            return bs4.BeautifulSoup(in_f, "html.parser")

    def test_simple_parse(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.union1")
        assert signature_text(sig) == "union union1 = type1 | type2"

    def test_links_member_types(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.union1")
        link = sig.a
        assert link, "Nested type did not resolve to a valid hyperlink"
        assert link.get_text() == "type1"

    def test_with_directive(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.union2")
        assert signature_text(sig) == "union union2 @directive1 = type1 | type2"

    def test_role(self, soup: bs4.BeautifulSoup):
        links = soup.find(id="roles").find_all("a", "reference")
        assert len(links) == 1
        link = links[0]
        assert link.get_text() == "schema1.union1"

    def test_docstrings(self, soup: bs4.BeautifulSoup):
        assert not soup.find("blockquote")

        sig = soup.find(id="schema1.union2")
        docstring = sig.parent.dd
        assert docstring.get_text().startswith(
            "union2 tests that directives are parsed.\n"
            "It also tests that multiline docstrings are formatted correctly."
        )


class TestRootDir:
    @pytest.fixture(scope="class")
    def soup(self, tmp_path_factory):
        cwd = pathlib.Path.cwd()
        root_dir = "schema"

        test_name = "type_objects"
        dest = tmp_path_factory.mktemp(test_name)
        (dest / root_dir).mkdir()
        test_file_name = f"{test_name}.graphql"
        test_file = pathlib.Path("tests") / "fixtures" / test_file_name
        shutil.copy(test_file, dest / root_dir)
        shutil.copy(pathlib.Path("tests") / "fixtures" / "conf.py", dest)

        with (dest / "index.rst").open("w") as out_f:
            out_f.write(f"Schema\n")
            out_f.write(f"------\n")
            out_f.write(f"\n")
            out_f.write(f".. autogqlschema:: schema1\n")
            out_f.write(f"   :debug:\n")
            out_f.write(f"   :root-dir: {root_dir}\n")
            out_f.write(f"   :source-files: {test_file_name}\n\n")

        os.chdir(dest)
        rebuild()

        with (pathlib.Path("_build") / "html" / "index.html").open() as in_f:
            yield bs4.BeautifulSoup(in_f, "html.parser")

        os.chdir(cwd)

    def test_simple_parse(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.type1")
        assert signature_text(sig) == "type type1"

        sig = soup.find(id="schema1.type1.field1")
        assert signature_text(sig) == "field1: Int"


class TestMarkdownProject:
    @pytest.fixture(scope="class")
    def soup(self, tmp_path_factory):
        cwd = pathlib.Path.cwd()

        test_name = "type_objects"
        dest = tmp_path_factory.mktemp(test_name)
        test_file_name = f"{test_name}.graphql"
        test_file = pathlib.Path("tests") / "fixtures" / test_file_name
        shutil.copy(test_file, dest)
        shutil.copy(pathlib.Path("tests") / "fixtures" / "conf.py", dest)

        with (dest / "conf.py").open("a") as out_f:
            out_f.write("extensions.append('myst_parser')\n")
            out_f.write("myst_enable_extensions = ['colon_fence']\n")

        with (dest / "index.md").open("w") as out_f:
            out_f.write(f"# Schema\n")
            out_f.write(f"\n")
            out_f.write(f"```{{autogqlschema}} schema1\n")
            out_f.write(f":debug:\n")
            out_f.write(f":source-files: {test_file_name}\n\n")
            out_f.write(f"```")

        os.chdir(dest)
        rebuild()

        with (pathlib.Path("_build") / "html" / "index.html").open() as in_f:
            yield bs4.BeautifulSoup(in_f, "html.parser")

        os.chdir(cwd)

    def test_simple_parse(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1.type1")
        assert signature_text(sig) == "type type1"

        sig = soup.find(id="schema1.type1.field1")
        assert signature_text(sig) == "field1: Int"
