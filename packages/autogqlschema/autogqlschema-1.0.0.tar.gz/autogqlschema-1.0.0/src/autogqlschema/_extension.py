from __future__ import annotations

import sphinx.application
import sphinx.util.logging

from ._directive import AutoGQLSchemaDirective

LOGGER = sphinx.util.logging.getLogger(__name__)


def setup(app: sphinx.application.Sphinx) -> dict[str, bool]:
    if not hasattr(app.config, "myst_enable_extensions"):
        setattr(app.config, "myst_enable_extensions", [])

    if "fieldlist" not in app.config.myst_enable_extensions:
        app.config.myst_enable_extensions.append("fieldlist")

    app.setup_extension("graphqldomain")
    app.setup_extension("myst_parser")
    app.add_directive("autogqlschema", AutoGQLSchemaDirective)

    return {
        "parallel_read_safe": True,
    }
