import stactools.core
from stactools.cli.registry import Registry

from stactools.msbuildings.stac import create_collection, create_item

__all__ = ["create_collection", "create_item"]

stactools.core.use_fsspec()


def register_plugin(registry: Registry) -> None:
    from stactools.msbuildings import commands

    registry.register_subcommand(commands.create_msbuildings_command)


__version__ = "0.2.0"
