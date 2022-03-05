from abc import ABCMeta, abstractmethod


class IDbGen:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_db_table(self, table_name, count_of_rows, columns_names):
        """Create specified table in database with using faker"""
        pass

    @abstractmethod
    def add_row_to(self, table_name, values):
        """Add values to specified table"""
        pass

    @abstractmethod
    def save_db_to_file(self):
        """Save database to .db file"""
        pass
