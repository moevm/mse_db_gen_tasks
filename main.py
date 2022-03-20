from db_gen.db_gen_class import DbGen
from db_tree.main import Tree


def main():
    db_generator = DbGen("dataBaseFile.db")
    tree = Tree()
    tree.loadJSON("save.json", db_generator)
    tree.saveJSON("save1.json")

    # db_generator.create_db_table("a", 5, ["name", "country"])
    # db_generator.create_db_table("b", 5, ['name', 'street_address', 'city', 'phone', 'email', 'year', 'date'])
    # db_generator.add_row_to("a", ["Boris", "Russia"])
    # db_generator.describe_db()


if __name__ == "__main__":
    main()
