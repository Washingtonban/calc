from sqlalchemy import Table, MetaData
from sqlalchemy.ext.declarative import declarative_base


class Base:
    __tablename__: str
    __table__: Table

    def get_primary_key_values_as_string(self) -> str:
        """Return the primary key values as string."""
        return ", ".join(
            [
                f"{column.name}={getattr(self, column.name)}"
                for column in self.__table__.primary_key.columns
            ]
        )

    def get_primary_key_values(self) -> dict[str]:
        """Return the primary key values as dict."""
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.primary_key.columns
        }

    def __repr__(self):
        """Return the object representation."""
        return f"<{self.__class__.__name__}({self.get_primary_key_values_as_string()})>"


convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referenced_table_name)s",
    "pk": "pk_%(table_name)s",
}


def DeclarativeBase(schema: str) -> Base:
    """Return a declarative base class."""
    return declarative_base(metadata=MetaData(schema=schema, naming_convention=convention))


class BaseHealth(Base, DeclarativeBase("health")):
    __abstract__ = True
    __table_args__ = {"extend_existing": True}
