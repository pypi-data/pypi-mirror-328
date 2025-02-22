from setuptools import setup, find_packages

setup(
    name="shared_db",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "sqlalchemy>=2.0.0",
        "pydantic>=2.0.0",
        "alembic>=1.14.0",
        "python-dotenv>=1.0.0",
        "psycopg2-binary>=2.9.0",
        # other dependencies
    ]
) 