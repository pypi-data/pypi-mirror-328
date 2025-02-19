"""All builtin sources."""
from .import op

@op.spec_class(op.OpCategory.SOURCE)
class LocalFile:
    """Import data from local file system."""

    path: str
    binary: bool = False
