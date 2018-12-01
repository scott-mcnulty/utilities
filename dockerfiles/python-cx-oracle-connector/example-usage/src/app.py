import connection.connection as connection


if __name__ == '__main__':

    query = 'SELECT 1 FROM DUAL'
    results = connection.execute_query(query)
    print(results)