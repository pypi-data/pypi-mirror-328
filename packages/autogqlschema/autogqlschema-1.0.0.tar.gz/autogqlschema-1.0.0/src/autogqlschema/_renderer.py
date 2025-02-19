import jinja2
import sphinx.util.logging

from ._objects import GraphQLObject

LOGGER = sphinx.util.logging.getLogger(__name__)


class JinjaRenderer:
    def __init__(self) -> None:
        self.env = jinja2.Environment(
            loader=jinja2.PackageLoader("autogqlschema", "_templates"),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        self._max_depths: list[int] = []

    def render(self, node: GraphQLObject) -> str:
        LOGGER.log("VERBOSE", "Rendering %s", node.signature)

        parent_max_depths = self._max_depths
        self._max_depths = []

        template = self.env.get_template(f"{node.type}.md.jinja")
        ctx = node.get_context_data()
        ctx["renderer"] = self
        result = template.render(**ctx)

        max_depth = max(self._max_depths, default=0)
        fence_length = max_depth
        result = "`" * fence_length + result.strip() + "`" * fence_length

        parent_max_depths.append(max_depth + 1)
        self._max_depths = parent_max_depths

        return result
