import random


class SelectRequestGenerator:
    def __init__(self):
        self.sort_directions = ["ASC", "DESC"]
        pass

    def generate_request(self, columns_list, table_name, include_sort=True):
        random_columns = list(set(random.choices(columns_list, k=random.randrange(1, len(columns_list)))))
        random_columns_str = ','.join(random_columns)

        columns_for_count = list(set(random.choices(random_columns, k=random.randrange(0, len(random_columns)+1))))
        columns_for_max = list(set(random.choices(random_columns, k=random.randrange(0, len(random_columns) + 1))))
        columns_for_min = list(set(random.choices(random_columns, k=random.randrange(0, len(random_columns) + 1))))
        columns_for_avg = list(set(random.choices(random_columns, k=random.randrange(0, len(random_columns) + 1))))
        columns_for_sum = list(set(random.choices(random_columns, k=random.randrange(0, len(random_columns) + 1))))

        for column in columns_for_count:
            random_columns_str = random_columns_str + ",COUNT(" + column + ")"
        for column in columns_for_max:
            random_columns_str = random_columns_str + ",MAX(" + column + ")"
        for column in columns_for_min:
            random_columns_str = random_columns_str + ",MIN(" + column + ")"
        for column in columns_for_avg:
            random_columns_str = random_columns_str + ",AVG(" + column + ")"
        for column in columns_for_sum:
            random_columns_str = random_columns_str + ",SUM(" + column + ")"

        request = 'SELECT ' + random_columns_str + " FROM " + table_name

        if include_sort:
            column_for_sort = random.choice(random_columns)
            sort_dir = random.choice(self.sort_directions)
            request = request + " ORDER BY " + column_for_sort + " " + sort_dir

        return request

    def save_request(self, query):
        file = open("./results/query", "w")
        file.write(query)
