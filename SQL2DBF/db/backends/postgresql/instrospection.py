from db.backends.base.introspection import (
    BaseDatabaseIntrospection, TableInfo
)


class DatabaseIntrospection(BaseDatabaseIntrospection):
    ignored_tables = []

    def get_table_list(self, cursor):
        """Return a list of table and view names in the current database."""
        cursor.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema='public'
            AND table_type='BASE TABLE';
        """)
        return [TableInfo(*row) for row in cursor.fetchall() if row[0] not in self.ignored_tables]

    def get_column_list(self, cursor, table_name):
        pass