import sqlite3

conn = sqlite3.connect("company_data.db")
cursor = conn.cursor()

# Get all user tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
tables = cursor.fetchall()

# Get row counts
for (table_name,) in tables:
    try:
        cursor.execute(f'SELECT COUNT(*) FROM "{table_name}"')
        count = cursor.fetchone()[0]
        print(f"{table_name}: {count} rows")
    except Exception as e:
        print(f"Error with table {table_name}: {e}")

conn.close()
