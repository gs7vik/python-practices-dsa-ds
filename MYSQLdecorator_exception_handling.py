import mysql.connector
from mysql.connector import Error as MySQLError

# Custom exceptions
class InvalidData(Exception):
    pass

class OperationFailed(Exception):
    pass

class ConnectError(Exception):
    pass

def handle_mysql_exception(func):
    def decorated_func(*args, **kwargs):
        try:
            # Assuming 'connection' is a MySQL connection object passed as an argument
            connection = args[0]
            result = func(*args, **kwargs)

        except mysql.connector.Error as e:
            if isinstance(e, mysql.connector.errors.DatabaseError):
                raise OperationFailed("Database operation failed")
            elif isinstance(e, mysql.connector.errors.InterfaceError):
                raise ConnectError("Connection error: Interface error")
            elif isinstance(e, mysql.connector.errors.IntegrityError):
                raise InvalidData("Data integrity error")
            elif isinstance(e, mysql.connector.errors.ProgrammingError):
                raise OperationFailed("Programming error")
            else:
                raise e

        return result

    return decorated_func

@handle_mysql_exception
def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# Usage
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="clovertex_master"
    )
    result = execute_query(connection, "SELECT  FROM healthcare")
    print(result)
except InvalidData as e:
    print(f"Invalid Data Error: {e}")
except OperationFailed as e:
    print(f"Operation Failed Error: {e}")
except ConnectError as e:
    print(f"Connect Error: {e}")
except mysql.connector.Error as e:
    print(f"MySQL Error: {e}")
finally:
    if connection:
        connection.close()

