import random

class SelectRequestGenerator:
    def __init__(self):
        pass

    def generate_request(self, columns_list, table_name):
        random_columns = list(set(random.choices(columns_list, k=random.randrange(1, len(columns_list)))))
        random_columns = ','.join(random_columns)
        request = 'SELECT ' + random_columns + " FROM " + table_name
        return request
