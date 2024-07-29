import streamlit as st
import snowflake.connector
import time
import logging
import sys
st.title('Log Table Data with Snowpark')

class SnowConnector:
    def __init__(self, creds):
        try:
            self.user = creds['user']
            self.account = creds['account']
            self.warehouse = creds['warehouse']
            self.database = creds['database']
            self.schema = creds['schema']
            self.password = creds['password']
            self.role = creds['role']
        except KeyError as e:
            raise ValueError(f'Missing credential key: {e}')

    def snowflake_cursor(self):
        e_counter = 0
        conn = None

        while e_counter < 5:
            try:
                conn = snowflake.connector.connect(
                    user=self.user,
                    password=self.password,
                    account=self.account,
                    role=self.role,
                    warehouse=self.warehouse,
                    database=self.database,
                    schema=self.schema
                )
                break
            except snowflake.connector.errors.DatabaseError as e:
                logging.error(f'Connection error: {e}. Retrying...')
                e_counter += 1
                time.sleep(5)
        if not conn:
            logging.error("Connection to Snowflake refused after 5 attempts.")
            sys.exit(1)
        logging.info("Connected to Snowflake")
        return conn

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    
    snow_creds = {
        "user": "HARDEEPSINGH2510",
        "password": "Gagan@2710",
        "account": "tr45041.ap-southeast-1",
        "role": "ACCOUNTADMIN",
        "warehouse": "COMPUTE_WH",
        "database": 'LOGS',
        "schema": 'PUBLIC'
    }

    snowflake_con = SnowConnector(creds=snow_creds)
    conn = snowflake_con.snowflake_cursor()
    cursor = conn.cursor()

    try:
        create_table='''create or replace table log_table(
    id INT AUTOINCREMENT PRIMARY KEY,
    timestamp TIMESTAMP,
    log_description STRING,
    log_type STRING
            )'''          
        cursor.execute(create_table)

        insert='''insert into log_table(timestamp,log_description,log_type)
        values (CURRENT_TIMESTAMP(), 'Unsigned TLS certificate signed authority', 'WARNING'),
        (CURRENT_TIMESTAMP(), 'Network latency detected', 'WARNING'),
        (CURRENT_TIMESTAMP(), 'Database connection timeout', 'ERROR'),
        (CURRENT_TIMESTAMP(), 'User login successful', 'INFO');'''
        cursor.execute(insert)

        cursor.execute('select *from log_table')
        rows=cursor.fetchall()

        st.dataframe(rows)

    except snowflake.connector.errors.ProgrammingError as e:
        logging.error(f"An error occurred: {e}")
    


    finally:
        cursor.close()
        conn.close()


    
