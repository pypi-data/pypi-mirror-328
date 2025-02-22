from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
import os
from dotenv import load_dotenv
import sys
from pathlib import Path

# Add the project root directory to Python path
project_root = str(Path(__file__).parents[2])  # Go up 2 levels from env.py
sys.path.append(project_root)

from shared_db.database import Database
from shared_db.models.base import Base

load_dotenv()
db = Database(
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    db_name=os.getenv("DB_NAME"),
)

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.
def include_name(name, type_, parent_names):
    """
    This function is used to determine which tables are included in the
    --autogenerate process.

    If you add a schema, please add it to the list below.

    """
    if type_ == "schema":
        if name in [None, "public"]:
            print(name, ' schema included in --autogenerate')
            return True
    else:
        return True


def include_object(object, name, type_, reflected, compare_to) -> bool:
    # Exclude tables ending with '_view'
    if type_ == 'table':
        if name in ['users']:
            print('excluding ', name)
            return False
    return True

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        include_name=include_name,
        include_object=include_object
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    import sqlalchemy as sa
    with db.engine.connect() as connection:
        print("Creating alembic schema")
        connection.execute(sa.text('CREATE SCHEMA IF NOT EXISTS alembic;'))
        connection.commit()

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            version_table_schema='alembic',
            include_schemas=True,
            include_name=include_name,
            include_object=include_object
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
