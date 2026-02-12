from connection import Connection

connection = Connection()


def select_many(query: str):
    conn = connection.get_connection()
    with conn.cursor(dictionary=True) as cursor:
        cursor.execute(f"USE {connection.database}")
        cursor.execute(query)
        result = cursor.fetchall()
    return result


def get_10_client_with_max_orders():
    query = """
    SELECT c.customerNumber, c.customerName, COUNT(o.orderNumber) as count
    FROM customers AS c INNER JOIN orders o
    ON c.customerNumber = o.customerNumber
    GROUP BY c.customerNumber, c.customerName
    ORDER BY count
    LIMIT 10
           """
    return select_many(query)

def get_client_withnt_ordres():
    query = """
    SELECT c.customerNumber, c.customerName, COUNT(o.orderNumber) as count
    FROM customers AS c LEFT JOIN orders o
    ON c.customerNumber = o.customerNumber
    GROUP BY c.customerNumber, c.customerName
    HAVING COUNT(o.orderNumber) = 0
            """
    return select_many(query)

def get_client_withnt_credit_limit():
    query = """
    SELECT c.customerNumber, c.customerName, c.creditLimit
        FROM customers  AS c INNER JOIN orders o
        ON c.customerNumber = o.customerNumber
        WHERE c.creditLimit = 0.0
        GROUP BY c.customerNumber, c.customerName
            """
    return select_many(query)




