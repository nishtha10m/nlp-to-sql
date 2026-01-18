import sqlite3
import pandas as pd

def load_to_sqlite(df, table_name="uploaded"):
    conn = sqlite3.connect("database.db")
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    return conn

def run_sql(conn, sql):
    return pd.read_sql_query(sql, conn)
