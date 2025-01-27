import pandas as pd
import psycopg2
from psycopg2 import extras
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Anslut till PostgreSQL-databasen
conn_params = {
    "host": "localhost",
    "database": "postgres",
    "user": "Bena88hox",
    "password": "Pipi-ina-18",
    "port": "5432"
}

csv_file_path = "sales_data.csv"  # Sökvägen till din CSV-fil

try:
    # Läs in CSV-filen
    df = pd.read_csv(csv_file_path, parse_dates=['Date'])
    logging.info(f"Läste in {len(df)} rader från CSV-filen.")
    print(f"Läste in {len(df)} rader från CSV-filen.")

    # Skapa tabellen i PostgreSQL om den inte redan finns
    create_table_query = """
    CREATE TABLE IF NOT EXISTS sales (
        id SERIAL PRIMARY KEY,
        date DATE,
        product VARCHAR(50),
        price NUMERIC,
        quantity INTEGER,
        sales NUMERIC
    );
    """

    with psycopg2.connect(**conn_params) as conn:
        logging.info("Ansluten till PostgreSQL-databasen.")
        print("Ansluten till PostgreSQL-databasen.")
        with conn.cursor() as cursor:
            cursor.execute(create_table_query)
            conn.commit()
            logging.info("Tabellen 'sales' skapades eller existerar redan.")
            print("Tabellen 'sales' skapades eller existerar redan.")

            # Förbered data för batch-insert
            rows = df.to_records(index=False).tolist()
            insert_query = """
            INSERT INTO sales (date, product, price, quantity, sales)
            VALUES %s
            """
            extras.execute_values(cursor, insert_query, rows)
            conn.commit()
            logging.info(f"{len(rows)} rader har importerats till PostgreSQL.")
            print(f"{len(rows)} rader har importerats till PostgreSQL.")

    logging.info("CSV-filen har importerats till PostgreSQL!")
    print("CSV-filen har importerats till PostgreSQL!")

except Exception as e:
    logging.error(f"Ett fel uppstod: {e}")
    print(f"Ett fel uppstod: {e}")