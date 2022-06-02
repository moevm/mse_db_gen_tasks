from main import MainGenerator
import click


@click.group()
def cli():
    pass


@click.command(name='gen_with_random_seed')
@click.option("--dump", default="nodump", type=str, help="dump database")
@click.option("-c", "--console", default=0, type=int, help="print in console")
def gen_with_random_seed(dump, console):
    main_gen = MainGenerator()
    main_gen.generate_tree_with_random_seed(console)
    if dump != "nodump":
        main_gen.dump_db(dump)


@click.command(name='gen_with_seed')
@click.option("-s", "--seed", default=0, type=int, help="set a seed for generator")
@click.option("-d", "--dump", default="nodump", type=str, help="dump database")
@click.option("-c", "--console", default=0, type=int, help="print in console")
def gen_with_seed(seed, dump, console):
    main_gen = MainGenerator()
    main_gen.generate_tree(seed, console)
    if dump != "nodump":
        main_gen.dump_db(dump)



@click.command(name='rel')
@click.option("-s", "--seed", default=0, type=int, help="set a seed for generator")
def gen_with_relations(seed):
    main_gen = MainGenerator()
    main_gen.generate_tree_with_relations(seed)


@click.command(name='gen_select_request')
@click.option("-w", default=False, help="add WHERE")
@click.option("-o", default=False, help="add ORDER BY")
@click.option("-c", "--console", default=0, type=int, help="print in console")
def gen_select_request(w, o, console):
    main_gen = MainGenerator()
    main_gen.generate_select_request(w, o, console)


cli.add_command(gen_select_request)
cli.add_command(gen_with_random_seed)
cli.add_command(gen_with_seed)
cli.add_command(gen_with_relations)

if __name__ == "__main__":
    cli()
