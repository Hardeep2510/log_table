# import requests
# def fetch_data_from_api(library):
#     url='https://pypi.org/project/library/'
#     try:
#         response=requests.get(url)
#         if response.status_code==200:
#             print('ho gaya')



# import streamlit as st
# import streamlit as st
# import snowflake.connector
# import time
# import logging
# import sys
# class SnowConnector:
#     def __init__(self, creds):
#         try:
#             self.user = creds['user']
#             self.account = creds['account']
#             self.warehouse = creds['warehouse']
#             self.database = creds['database']
#             self.schema = creds['schema']
#             self.password = creds['password']
#             self.role = creds['role']
#         except Exception as e:
#             print(e, '\nPlease check the credential file for missing information')

#     def snowflake_cursor(self):
#         e_counter = 0
#         conn = None

#         while e_counter < 5:
#             try:
#                 conn = snowflake.connector.connect(
#                     user=self.user,
#                     password = self.password,
#                     account=self.account,
#                     role = self.role, 
#                     warehouse=self.warehouse,
#                     database=self.database,
#                     schema=self.schema
#                 )
#                 break
#             except snowflake.connector.errors.DatabaseError as e:
#                 print(e)
#                 print('Connection to Snowflake refused, trying again...')
#                 e_counter += 1
#                 time.sleep(5)
#         if not conn:
#             print("""\n*****\n
#                      Connection to Snowflake refused after 5 attempts.  
#                     Please check connection credentials and  
#                     connection to server/internet.
#                      \n*****\n""")
#             exit(1)
#         print("Connected to Snowflake")
#         return conn
    


# if __name__=='__main__':
#     snow_creds = {"user":"HARDEEPSINGH2510",
#             'password':"Gagan@2710", 
#             "account":"tr45041.ap-southeast-1",
#             "role":"ACCOUNTADMIN",  
#             "warehouse":"COMPUTE_WH",
#             "database":'LOGS',
#             "schema": 'PUBLIC'
#             }
#     snowflake_con = SnowConnector(creds=snow_creds)
#     conn = snowflake_con.snowflake_cursor()
#     cursor=conn.cursor()

#     try:
#         create_table='''
#                 create or replace log_table(
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 timestamp DATETIME,
#                 log_description varchar(255),
#                 log_type ENUM('INFO','WARNING','ERROR')
#                 )
#         '''
#         cursor.execute(create_table)
#     except snowflake.connector.errors.ProgrammingError as e:
#         print(f"An error occurred: {e}")

#     finally:
#         cursor.close()
#         conn.close()



import snowflake.connector
import time
import logging
import streamlit as st

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
        "database": 'TESTS',
        "schema": 'PUBLIC'
    }

    snowflake_con = SnowConnector(creds=snow_creds)
    conn = snowflake_con.snowflake_cursor()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE OR REPLACE TABLE log_table (
        id INT AUTOINCREMENT PRIMARY KEY,
        timestamp TIMESTAMP,
        log_description STRING,
        CONSTRAINT log_type STRING CHECK (log_type IN ('INFO', 'WARNING', 'ERROR'))
        ) IN snowflake connector for python
            """)
    cursor.close()
    conn.close()



    
