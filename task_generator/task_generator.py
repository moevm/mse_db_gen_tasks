from fpdf import FPDF

from db_gen.classes.db_gen_class import DbGen
from select_request_generator.select_request_gen import SelectRequestGenerator
from db_tree.db_query import dbQuery

class TaskGenerator:
    def __init__(self, db_gen_path='../results/db_f.db'):
        self.db_gen = DbGen(db_gen_path)
        self.select_request_generator = SelectRequestGenerator(self.db_gen)
        self.db_query = dbQuery(db_gen_path)

    def generate_task(self, pdf_path=None):
        table, columns = self.db_gen.get_random_table_with_columns()
        query = self.select_request_generator.generate_request(columns_list=columns, table_name=table)
        print(DbGen.parse_query(query))
        self.db_query.printTables()
        if pdf_path is not None:
            pdf = FPDF()
            pdf.add_page()
            pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
            pdf.set_font('DejaVu', '', 8)
            pdf.multi_cell(0, 5, txt=DbGen.parse_query(query))
            self.db_query.write_to_pdf(pdf=pdf, path=pdf_path)
