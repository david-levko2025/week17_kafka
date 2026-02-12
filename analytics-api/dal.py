def get_10_client_with_max_orders():
    query = """
    SELECT customers.customerName,
    COUNT(order.orderNumber) 
    FROM customers
     
            """
    return query

def get_client_withnt_ordres():
    query = """
    SELECT customers.customerName FROM customers
    INNER JOIN order.customerNumber
    ON order.customerNumber = customers.customerNumber
    WHERE COUNT(order.orderNumber) < 1
            """
    return query

def get_client_withnt_credit_limit():
    query = """
    SELECT customers.customerName FROM customers
            """
    return query