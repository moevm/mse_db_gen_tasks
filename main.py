from db_gen.classes.db_gen_class import DbGen


def main():
    db_generator = DbGen("dataBaseFile.db")
    # db_generator.create_db_table("a", 5, ["name", "country"])
    # db_generator.add_row_to("a", ["Boris", "Russia"])


if __name__ == "__main__":
    main()
