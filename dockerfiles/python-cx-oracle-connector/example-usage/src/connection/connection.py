import cx_Oracle

import connection.connection_config as connection_config
connection = cx_Oracle.connect(connection_config.MAIN_CONNECT_STRING)

def execute_query(query):
	'''
	Run generic query
	'''

	cursor = connection.cursor()
	cursor.execute(query)
	res = cursor.fetchall()
	return res
