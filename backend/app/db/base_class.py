from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData

# Recommended naming convention used by Alembic, as recommended in the
# latest SQLAlchemy documentation
# See: https://alembic.sqlalchemy.org/en/latest/naming.html
NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

# Create a metadata object with the naming convention
metadata = MetaData(naming_convention=NAMING_CONVENTION)

class Base(DeclarativeBase):
    """
    Base class for SQLAlchemy models.
    Includes metadata with naming conventions for Alembic autogenerate.
    """
    metadata = metadata
