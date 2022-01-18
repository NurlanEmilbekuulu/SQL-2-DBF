from db.backends.base.base import BaseDatabaseWrapper
from db.backends.postgresql.instrospection import DatabaseIntrospection

try:
    import psycopg2 as Database
except ImportError as e:
    raise Exception("Error loading psycopg2 module: %s" % e)


class DatabaseWrapper(BaseDatabaseWrapper):
    """Represent a PostgreSQL database connection."""

    data_types = {}

    Database = Database
    introspection_class = DatabaseIntrospection

    def get_connection_params(self):
        conn_params = {}
        return conn_params

    def get_new_connection(self, conn_params):
        connection = Database.connect(**conn_params)
        return connection
