from abc import ABCMeta, abstractmethod


class IDbGen:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_db_table(self, table_name, count_of_rows, columns_names):
        """
        Create specified table in database with using faker
        :param table_name: Table's name which you want create it with
        :param count_of_rows: Count of rows that will be generated with faker
        :param columns_names: Array of names that can be provided by faker
        """
        pass

    @abstractmethod
    def add_row_to(self, table_name, values):
        """
        Add values to specified table
        :param values: You need to know what columns have in the table you want insert values to
        """
        pass

    @abstractmethod
    def save_db_to_file(self):
        """Save database to .db file"""
        pass
