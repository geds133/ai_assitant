import sqlite3
from langchain.tools import Tool

def list_tables():
    with sqlite3.connect(r'src\agents\db.sqlite') as conn:
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return "\n".join(row[0] for row in c.fetchall() if row[0] is not None)

def run_sqlite_query(query):
    with sqlite3.connect(r'src\agents\db.sqlite') as conn:
        c = conn.cursor()
        c.execute(query)
        return c.fetchall()

run_query_tool = Tool.from_function(
    name='run_sqlite_query',
    description="Run a sqlite query.",
    func=run_sqlite_query
)

def describe_tables(tables_name):
    with sqlite3.connect(r'src\agents\db.sqlite') as conn:
        c = conn.cursor()
        tables = ', '.join("'" + table + "'" for table in tables_name)
        c.execute(f'SELECT sql FROM sqlite_master WHERE type="table" AND name IN ({tables});')
        return "\n".join(row[0] for row in c.fetchall() if row[0] is not None)

describe_tables_tool = Tool.from_function(
    name='describe_tables',
    description='Lists the tables and returns the schema.',
    func=describe_tables
)