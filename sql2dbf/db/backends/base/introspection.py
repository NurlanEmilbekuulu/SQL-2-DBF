from collections import namedtuple

# Structure returned by DatabaseIntrospection.get_table_list()
TableInfo = namedtuple('TableInfo', 'name')


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
