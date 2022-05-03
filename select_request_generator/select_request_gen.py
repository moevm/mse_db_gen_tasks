import random

class SelectRequestGenerator:
    def __init__(self):
        pass

    def generate_request(self, columns_list, table_name):
        random_columns = ','.join(random.randrange(0, len(columns_list) - 1))
        request = 'SELECT ' + random_columns + " FROM " + table_name;
        return request
