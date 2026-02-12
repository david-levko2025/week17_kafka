import os
import mysql.connector


config = {
            'host': os.getenv("MYSQL_HOST", "localhost"),
            'port': int(os.getenv("MYSQL_PORT", "3306")),
            'user': os.getenv("MYSQL_USER", "root"),
            'password': os.getenv("MYSQL_PASS", "")
        }
database = os.getenv("MYSQL_DB", "weapon_db")
connection = None

def get_connection(self):
    connection = mysql.connector.connect(config)

    if not connection.is_connected:
            raise ConnectionError("Couldn't connect to the database")
    return connection

def create_tables(self):
    conn = get_connection()
    create_customer = """
                CREATE TABLE IF NOT EXISTS customers (
                customerNumber INT PRIMARY KEY,
                customerName VARCHAR(255),
                contactLastName VARCHAR(255),
                contactFirstName VARCHAR(255),
                phone VARCHAR(15),
                addressLine1 VARCHAR(255),
                addressLine2 VARCHAR(255),
                city VARCHAR(255),
                state VARCHAR(255),
                postalCode VARCHAR(255),
                country VARCHAR(255),
                salesRepEmployeeNumber INT,
                creditLimit FLOAT
                )"""

    create_order = """
                        CREATE TABLE IF NOT EXISTS orders (
                        orderNumber INT PRIMARY KEY,
                        orderDate DATE,
                        requiredDate DATE,
                        shippedDate DATE,
                        status VARCHAR(50),
                        comments VARCHAR(255),
                        FOREIGN KEY (customerNumber) REFERENCES customers(customerNumber)
                        )"""

    with conn.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
        cursor.execute(f"USE {database}")
        cursor.execute(create_customer)
        cursor.execute(create_order)
        connection.commit()

def insert_customer(customer):
    conn = get_connection()
    insert_statement = """INSERT INTO customers (
                    customerNumber, customerName, contactLastName, contactFirstName,
                    phone, addressLine1, addressLine2, city, state,
                    postalCode, country, salesRepEmployeeNumber, creditLimit)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """

    with conn.cursor() as cursor:
            cursor.execute(f"USE {database}")
            cursor.execute(insert_statement, customer)
            conn.commit()
    return {
            "status": "success",
           }

def insert_order(order):
    conn = get_connection()
    insert_statement = """INSERT INTO orders (
                    orderNumber, CAST(orderDate AS DATE), CAST(requiredDate AS DATE),
                    CAST(shippedDate AS DATE), status, comments, customerNumber)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """

    with conn.cursor() as cursor:
        cursor.execute(f"USE {database}")
        cursor.execute(insert_statement, order)
        conn.commit()
    return {
            "status": "success",
           }