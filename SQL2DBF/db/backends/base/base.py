class BaseDatabaseWrapper:
    """Represent a database connection."""

    data_types = {}
    introspection_class = None

    def __init__(self, settings_dict):
        self.connection = None
        self.settings_dict = settings_dict

    def get_connection_params(self):
        """Return a dict of parameters suitable for get_new_connection."""
        raise NotImplementedError('subclasses of BaseDatabaseWrapper may require a get_connection_params() method')

    def get_new_connection(self, conn_params):
        """Open a connection to the database."""
        raise NotImplementedError('subclasses of BaseDatabaseWrapper may require a get_new_connection() method')
