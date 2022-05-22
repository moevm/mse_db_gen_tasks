import os
import sqlite3
from prettytable import PrettyTable

from fpdf import FPDF

class dbQuery:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)

        self.cur = self.conn.cursor()
        self.tables = []
        self.cur.execute('SELECT name from sqlite_master where type= "table"')
        for table in self.cur:
            self.tables.append(table[0])
        self.query = None

    def queryToDB(self, query):
        # self.cur.execute('SELECT name from sqlite_master where type= "table"')
        #
        # print(self.cur.fetchall())
        self.query = query
        self.cur.execute(query)

    def printQuery(self):
        if self.query is not None:
            columns = self.cur.description
            th = []
            for row in columns:
                th.append(row[0])
            table = PrettyTable(th)
            td = self.cur.fetchall()
            table.add_rows(td)
            print(table)

    def get_pretty_tables(self):
        pretty_tables = []
        for table_name in self.tables:
            query = 'SELECT * FROM ' + table_name
            self.cur.execute(query)
            columns = self.cur.description
            th = []
            for row in columns:
                th.append(row[0])
            table = PrettyTable(th)
            table.title = table_name
            td = self.cur.fetchall()
            table.add_rows(td)
            pretty_tables.append(table)
        return pretty_tables

    def printTables(self):
        for pretty_table in self.get_pretty_tables():
            print(pretty_table)

    def get_data_from_pretty_table(self, pretty_table: PrettyTable):
        str = pretty_table.get_string().split('\n')
        header = str[1].replace(' ', '')[1: -1]
        rows = []
        for row in str[3: len(str) - 1]:
            data = row.replace(' ', '').split('|')[1: -1]
            rows.append(data)
        rows.pop(1)

        col_widths = []
        for col in range(len(rows[0])):
            max_str_len = 0
            for row in range(len(rows)):
                if max_str_len < len(rows[row][col]):
                    max_str_len = len(rows[row][col])
            col_widths.append(max_str_len)

        return header, rows, col_widths

    def write_to(self, path):
        pdf = FPDF()
        font_size = 8
        pdf.set_font(family="Arial")
        pdf.set_font_size(size=font_size)
        epw = pdf.w - 2 * pdf.l_margin
        row_height = pdf.font_size * 1.5
        spacing = 1.3

        for pretty_table in self.get_pretty_tables():
            header, data, col_widths = self.get_data_from_pretty_table(pretty_table)
            col_widths = [col + font_size * 1.5 for col in col_widths]

            table_width = sum(col_widths)
            free_space = epw - table_width
            if free_space > 0:
                pdf.add_page(orientation='portrait')
            else:
                pdf.add_page(orientation='landscape')
                free_space = pdf.w - 2 * pdf.l_margin - table_width

            ratio = free_space / (sum(col_widths))
            for col_index in range(len(col_widths)):
                table_width += col_widths[col_index] * ratio
                col_widths[col_index] += col_widths[col_index] * ratio

            pdf.cell(table_width, row_height * spacing, txt=header, border=1, align='C')
            pdf.ln(row_height * spacing)
            for row in data:
                for item_index in range(len(row)):
                    pdf.cell(col_widths[item_index], row_height*spacing, txt=row[item_index], border=1, align='C')
                pdf.ln(row_height * spacing)
        pdf.output(path)
        pdf.close()

    def printTableNames(self):
        for name in self.tables:
            print(name)

    def saveQuery(self, path):
        if self.query is not None:
            saveFile = open(path, "w+")
            saveFile.write(self.query)
            saveFile.close()


if __name__ == "__main__":
    db_query = dbQuery("/home/EFFECT322/PycharmProjects/mse_db_gen_tasks/results/db_f.db")
    db_query.printTables()
    db_query.write_to('test.pdf')
