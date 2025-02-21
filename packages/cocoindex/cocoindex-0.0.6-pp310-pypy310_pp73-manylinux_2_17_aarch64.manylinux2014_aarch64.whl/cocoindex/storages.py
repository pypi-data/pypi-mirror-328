"""All builtin storages."""
from . import op

@op.spec_class(op.OpCategory.STORAGE)
class Postgres:
    """Storage powered by Postgres and pgvector."""

    database_url: str | None = None
    table_name: str | None = None
