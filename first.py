import streamlit as st
import snowflake.connector
import time
import logging
import sys
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
        except Exception as e:
            print(e, '\nPlease check the credential file for missing information')

    def snowflake_cursor(self):
        e_counter = 0
        conn = None

        while e_counter < 5:
            try:
                conn = snowflake.connector.connect(
                    user=self.user,
                    password = self.password,
                    account=self.account,
                    role = self.role, 
                    warehouse=self.warehouse,
                    database=self.database,
                    schema=self.schema
                )
                break
            except snowflake.connector.errors.DatabaseError as e:
                print(e)
                print('Connection to Snowflake refused, trying again...')
                e_counter += 1
                time.sleep(5)
        if not conn:
            print("""\n*****\n
                     Connection to Snowflake refused after 5 attempts.  
                    Please check connection credentials and  
                    connection to server/internet.
                     \n*****\n""")
            exit(1)
        print("Connected to Snowflake")
        return conn
    


if __name__=='__main__':
    snow_creds = {"user":"HARDEEPSINGH2510",
            'password':"Gagan@2710", 
            "account":"tr45041.ap-southeast-1",
            "role":"ACCOUNTADMIN",  
            "warehouse":"COMPUTE_WH",
            "database":'TESTS',
            "schema": 'PUBLIC'
            }
    snowflake_con = SnowConnector(creds=snow_creds)
    conn = snowflake_con.snowflake_cursor()
    cursor=conn.cursor()
    cursor.execute('Select * from EMPLOYEES')
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    