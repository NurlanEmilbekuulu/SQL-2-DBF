from collections import namedtuple

# Structure returned by DatabaseIntrospection.get_table_list()
TableInfo = namedtuple('TableInfo', 'name')

# Structure returned by the DB-API cursor.description interface (PEP 249)
FieldInfo = namedtuple(
    'FieldInfo',
    'name type_code display_size internal_size precision scale null_ok '
    'default collation'
)


class BaseDatabaseIntrospection:
    """Encapsulate backend-specific introspection utilities."""
    data_types_reverse = {}

    def __init__(self, connection):
        self.connection = connection

    def get_table_list(self, cursor):
        """
        Return an unsorted list of TableInfo named tuples of all tables and
        views that exist in the database.
        """
        raise NotImplementedError('subclasses of BaseDatabaseIntrospection may require a get_table_list() method')

    def get_table_description(self, cursor, table_name):
        """
        Return a description of the table with the DB-API cursor.description
        interface.
        """
        raise NotImplementedError(
            'subclasses of BaseDatabaseIntrospection may require a '
            'get_table_description() method.'
        )
