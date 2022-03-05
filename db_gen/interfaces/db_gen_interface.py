from abc import ABCMeta, abstractmethod


class IDbGen:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_db_table(self, count_of_columns):
        """Create specified table in database"""
        pass

    @abstractmethod
    def add_row_to(self, table_name, values):
        """Add values to specified table"""
        pass

    @abstractmethod
    def save_db_to_file(self):
        """Save database to .db file"""
        pass
